from django.shortcuts import render
from django.views import View

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.db.models.deletion import ProtectedError

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
                return JsonResponse(data={'error': 'Ошибка'}, status=400)


    def get(self, request):
        form = ProfessionForm()
        context = {'add_prof_form': ProfessionForm()}
        render(request, 'task_app/base.html', context=context)


class DelProfession(View):
    def post(self, request, prof_pk):
        form_data = self.request.POST
        try:
            form_data = Profession.objects.filter(pk=prof_pk).delete()
            return JsonResponse(data={'deleted_pk': prof_pk}, status=201)
        except ProtectedError as e:
            return JsonResponse(data={'error': 'Ошибка удаления. Сначала необходимо удалить сотрудников, привязанных к этой профессии'}, status=400)


