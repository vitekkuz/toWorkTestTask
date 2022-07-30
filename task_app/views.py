from django.shortcuts import render
from django.views import View

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.db.models.deletion import ProtectedError
from django.db.utils import IntegrityError

from .forms import ProfessionForm, UserForm
from .models import User, Aria, District, City, PhoneNumber, Profession, Sex


def index(request):

    users = User.objects.all()
    surnames = users.all().values('surname').distinct()
    middle_names = users.all().values('middle_name').distinct()
    first_names = users.all().values('first_name').distinct()
    # get address list unique
    address_list = list(set([a.get_address() for a in users]))

    professions = Profession.objects.all()
    phoneNumbers = PhoneNumber.objects.all()
    cities = City.objects.all()
    arias = Aria.objects.all()
    districts = District.objects.all()
    sex = Sex.objects.all()
    context = {'users': users,
               'surnames': surnames,
               'middle_names': middle_names,
               'first_names': first_names,
               'address_list': address_list,
               'professions': professions,
               'phoneNumbers': phoneNumbers,
               'cities': cities,
               'arias': arias,
               'sex': sex,
               'districts': districts,
               'add_prof_form': ProfessionForm(),
               'modify_prof_form': ProfessionForm(),
               'form_add_user': UserForm(),
               }

    return render(request, 'task_app/base.html', context=context)


class AddProfession(View):
    def post(self, request):
        form_data = ProfessionForm(self.request.POST)

        if form_data.is_valid():
            new_prof, created = Profession.objects.get_or_create(text=form_data.cleaned_data['text'])

            if created:
                data = {'npk': new_prof.pk, 'ntext': new_prof.text, 'user_set': new_prof.count_users()}
                # print(new_prof)
                # print(data)
                # print('test')
                return JsonResponse(data=data, status=201)
            # СЮДА НУЖНО БУДЕТ ДОБАВИТЬ СООБЩЕНИЕ О ТОМ, ЧТО НИЧЕГО НЕ ДОБАВЛЕНО
            else:
                return JsonResponse(data={'error': 'Ошибка'}, status=400)


    # def get(self, request):
    #     form = ProfessionForm()
    #     context = {'add_prof_form': form}
    #     return render(request, 'task_app/base.html', context=context)


class ModifyProfession(View):
    def post(self, request, prof_data):
        form_data = ProfessionForm(self.request.POST)
        if form_data.is_valid():
            prof = Profession.objects.get(pk=prof_data)

            if prof:
                try:
                    prof.text = form_data.cleaned_data['text']
                    prof.save()
                except IntegrityError as e:
                    return JsonResponse(data={'error': 'Такая профессия уже существует'}, status=400)

                data = {'cur_pk': prof.pk, 'ntext': prof.text}
                # print(form_data)
                print(data)
                # print('test')
                return JsonResponse(data=data, status=201)
            else:
                return JsonResponse(data={'error': 'Ошибка'}, status=400)


    # def get(self, request):
    #     form = ProfessionForm()
    #     context = {'prof_form': form}
    #     return render(request, 'task_app/base.html', context=context)


class DelProfession(View):
    def post(self, request, prof_pk):
        form_data = self.request.POST
        try:
            form_data = Profession.objects.filter(pk=prof_pk).delete()
            return JsonResponse(data={'deleted_pk': prof_pk}, status=201)
        except ProtectedError as e:
            return JsonResponse(data={'error': 'Ошибка удаления. Сначала необходимо удалить сотрудников, привязанных к этой профессии'}, status=400)


class AddUser(View):
    def post(self, request):
        form_data = UserForm(self.request.POST)

        if form_data.is_valid():

            # try:
            new_phone, phone_created = PhoneNumber.objects.get_or_create(phoneNumber=form_data.cleaned_data['phoneNumber'])
            if phone_created:
                print('Создан номер телефона: ', new_phone)
            else:
                print('Номер уже был')
            if phone_created:
                new_user = User.objects.create(
                    surname=form_data.cleaned_data['surname'],
                    middle_name=form_data.cleaned_data['middle_name'],
                    first_name=form_data.cleaned_data['name'],
                    sex=Sex.objects.get(sex=form_data.cleaned_data['sex']),
                    age=form_data.cleaned_data['age'],
                    phoneNumber=PhoneNumber.objects.get(phoneNumber= form_data.cleaned_data['phoneNumber']),
                    profession=Profession.objects.get(text=form_data.cleaned_data['profession'])  ,
                    area= Aria.objects.get(text= form_data.cleaned_data['area']),
                    district=District.objects.get(text= form_data.cleaned_data['district']),
                    city=City.objects.get(text= form_data.cleaned_data['city'])
                )
            else:
                return JsonResponse(data={'error': 'Введен существующий номер телефона'}, json_dumps_params={'ensure_ascii': False}, status=400)

            # data = new_user # {'ntext': new_user}
            nuser= User.objects.latest("pk")
            return JsonResponse(data={
                'pk': nuser.pk,
                'surname': nuser.surname,
                'first_name': nuser.first_name,
                'middle_name': nuser.middle_name,
                'sex': str(nuser.sex),
                'age': nuser.age,
                'phoneNumber': str(nuser.phoneNumber),
                'profession': str(nuser.profession),
                'area': str(nuser.area),
                'district': str(nuser.district),
                'city': str(nuser.city)
            }, json_dumps_params={'ensure_ascii': False}, safe=False, status=201)
            # except :
            #     # print(new_prof)
            #     # print(data)
            #     # print('test')
            #     return JsonResponse(data={'error': 'e' }, status=400)
            # СЮДА НУЖНО БУДЕТ ДОБАВИТЬ СООБЩЕНИЕ О ТОМ, ЧТО НИЧЕГО НЕ ДОБАВЛЕНО
        else:
            return JsonResponse(data={'error': 'Ошибка'}, status=400)


class DelUser(View):
    def post(self, request, user_pk):
        form_data = self.request.POST
        try:
            form_data = User.objects.filter(pk=user_pk).delete()
            return JsonResponse(data={'deleted_pk': user_pk}, status=201)
        except:
            return JsonResponse(data={'error': 'Ошибка удаления!'}, status=400)


class ModifyUser(View):
    def post(self, request, user_pk):
        form_data = UserForm(self.request.POST)
        if form_data.is_valid():
            user = User.objects.get(pk=user_pk)

            if user:
                new_phone, phone_created = PhoneNumber.objects.get_or_create(
                    phoneNumber=form_data.cleaned_data['phoneNumber'])
                user.surname = form_data.cleaned_data['surname']
                user.middle_name = form_data.cleaned_data['middle_name']
                user.first_name = form_data.cleaned_data['name']
                user.sex = Sex.objects.get(sex=form_data.cleaned_data['sex'])
                user.age = form_data.cleaned_data['age']
                if phone_created:
                    user.phoneNumber = PhoneNumber.objects.get(phoneNumber=form_data.cleaned_data['phoneNumber'])
                user.profession = Profession.objects.get(text=form_data.cleaned_data['profession'])
                user.area = Aria.objects.get(text=form_data.cleaned_data['area'])
                user.district = District.objects.get(text=form_data.cleaned_data['district'])
                user.city = City.objects.get(text=form_data.cleaned_data['city'])
                user.save()

                return JsonResponse(data={
                    'pk': user.pk,
                    'surname': user.surname,
                    'first_name': user.first_name,
                    'middle_name': user.middle_name,
                    'sex': str(user.sex),
                    'age': user.age,
                    'phoneNumber': str(user.phoneNumber),
                    'profession': str(user.profession),
                    'area': str(user.area),
                    'district': str(user.district),
                    'city': str(user.city)
                }, json_dumps_params={'ensure_ascii': False}, safe=False, status=201)
            else:
                return JsonResponse(data={'error': 'Ошибка! Сотрудник не найден в базе!'}, status=400)