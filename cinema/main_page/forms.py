from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from phonenumber_field.formfields import PhoneNumberField
from user.models import ProjectUser


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input form_input', 'placeholder': "Username"}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input form_input', 'placeholder': "Password"}))


class CustomUserCreationForm(UserCreationForm):
    CHOICES_LANGUAGE = (('UKR', 'UKR'), ('ENG', 'ENG'),)
    CHOICES_SEX = (('MALE', 'MALE'), ('FEMALE', 'FEMALE'),)
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-input form_input', 'placeholder': "Username"}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-input form_input', 'placeholder': "Password"}))
    password2 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-input form_input', 'placeholder': "Repeat password"}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-input form_input', 'placeholder': "Last Name"}))
    anonym = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-input form_input', 'placeholder': "Anonym"}))
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'form-input form_input', 'placeholder': "E-mail"}))
    language = forms.CharField(widget=forms.Select(choices=CHOICES_LANGUAGE, attrs={'class': 'form-input form_input checkbox_input'},))
    sex = forms.CharField(
        widget=forms.Select(choices=CHOICES_SEX, attrs={'class': 'form-input form_input checkbox_input'}, ))
    phone = PhoneNumberField(widget=forms.TextInput(attrs={'class': 'form-input form_input', 'placeholder': "+380974536593"}))
    data_birthday = forms.DateField(widget=forms.DateInput(attrs={'placeholder': "Year-mounth-data", 'class': 'form-input form_input data_input'}))
    adress = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-input form_input', 'placeholder': "Adress"}))
    card_number = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-input form_input', 'placeholder': "1111 1111 1111 1111"}))
    choice_city = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-input form_input', 'placeholder': "City"}))
    class Meta:
        model = ProjectUser
        fields = ('username', 'last_name', 'anonym', 'email',  'password1', 'password2',  'language', 'sex', 'phone','data_birthday','adress', 'card_number', 'choice_city')

#'choice_city''card_number','adress','data_birthday' 'type': 'date',
# class CustomUserChangeForm(UserChangeForm):
#     class Meta:
#         model = ProjectUser
#         fields = (
#         'username', 'last_name', 'anonym', 'email', 'adress', 'password1', 'password2', 'card_number', 'language',
#         'sex', 'phone', 'data_birthday', 'choice_city')
