from django import forms
from .models import Aria, District, City, Profession


class ProfessionForm(forms.Form):
    text = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        ),
        label='Введите название',
        max_length=150,
    )


# ============== Пользователь ===================================
class UserForm(forms.Form):
    surname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': "surnameInput"
            }
        ),
        label='Фамилия',
        max_length=100,
    )
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': "nameInput"
            }
        ),
        label='Имя',
        max_length=100,
    )
    middle_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': "middleNameInput"
            }
        ),
        label='Отчество',
        max_length=100,
    )

    SEX = [
        ('М', 'Мужчина'),
        ('Ж', 'Женщина')
    ]
    sex = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': "sexInput"
            }
        ),
        label='Пол',
        choices=SEX,
    )
    age = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': "ageInput"
            }
        ),
        label='Возраст',
        max_length=2,
    )

    phoneNumber = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': "phoneInput"
            }
        ),
        label='Номер телефона',
        max_length=16,
    )
    PROFESSIONS = [(a.text, a.text) for a in  Profession.objects.all()]
    profession = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': "professionInput"
            }
        ),
        label='Профессия',
        choices=PROFESSIONS,
    )


    ARIES = [(a.text, a.text) for a in  Aria.objects.all()]
    area = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': "ariaInput"
            }
        ),
        label='Область',
        choices=ARIES,
    )
    DISTRICTS = [(a.text, a.text) for a in  District.objects.all()]
    district = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': "districtInput"
            }
        ),
        label='Район',
        choices=DISTRICTS,
    )
    CITIES = [(a.text, a.text) for a in  City.objects.all()]
    city = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': "cityInput"
            }
        ),
        label='Город',
        choices=CITIES,
    )




