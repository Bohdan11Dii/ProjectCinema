from django import forms
from django.contrib.auth.forms import UserCreationForm

from user.models import ProjectUser


class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(label='Логін', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    repeat_password = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label='Прізвище', widget=forms.TextInput(attrs={'class': 'form-input'}))
    anonym = forms.CharField(label='Псевдонім', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.CharField(label='E-mail', widget=forms.TextInput(attrs={'class': 'form-input'}))
    adress = forms.CharField(label='Адреса', widget=forms.TextInput(attrs={'class': 'form-input'}))
    card_number = forms.CharField(label='Номер картки', widget=forms.TextInput(attrs = {'class': 'form-input'}))
    language = forms.BooleanField(label='Язик', widget=forms.CheckboxInput())
    sex = forms.BooleanField(label='Стать', widget=forms.CheckboxInput())
    phone = forms.IntegerField(label='Номер телефону', widget=forms.NumberInput())
    birthday = forms.DateField(label='День народження', widget=forms.DateInput(format='%d/%m/%Y'))
    choice_city = forms.CharField(label='Вибір міста', widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = ProjectUser
        fields = ('username', 'password', 'repeat_password','last_name','anonym','email','adress','card_number','language','sex','phone','birthday','choice_city')
