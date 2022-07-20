from django.shortcuts import render
from django.views import View

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from .forms import ProfessionForm

from .models import User, Aria, District, City, PhoneNumber, Profession

# Create your views here.

def index(request):

    users = User.objects.all()
    professions = Profession.objects.all()
    phoneNumbers = PhoneNumber.objects.all()
    cities = City.objects.all()
    arias = Aria.objects.all()
    districts = District.objects.all()
    context = {'users': users,
               'professions': professions,
               'phoneNumbers': phoneNumbers,
               'cities': cities,
               'arias': arias,
               'districts': districts,
               'add_prof_form': ProfessionForm(),
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
                return JsonResponse(data={'error': 'какая-то ошибка'}, status=400)


    def get(self, request):
        form = ProfessionForm()
        context = {'add_prof_form': ProfessionForm()}
        render(request, 'task_app/base.html', context=context)

class AddProfession1(View):
    def post(self, request):
        form_data = ProfessionForm(self.request.POST)

        if form_data.is_valid():
            new_prof, created = Profession.objects.get_or_create(text=form_data.cleaned_data['text'])

            if created:
                data = {'npk': new_prof.pk, 'ntext': new_prof.text}
                print(data)
                return JsonResponse(data=data, status=201)
            # СЮДА НУЖНО БУДЕТ ДОБАВИТЬ СООБЩЕНИЕ О ТОМ, ЧТО НИЧЕГО НЕ ДОБАВЛЕНО
            else:
                return JsonResponse(data={'error': 'какая-то ошибка'}, status=400)

