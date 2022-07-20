from django import forms


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