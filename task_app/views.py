from django.shortcuts import render

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
               }


    return render(request, 'task_app/base.html', context=context)