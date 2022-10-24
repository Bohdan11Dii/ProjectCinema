from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class ProjectUser(AbstractUser):
    username = models.CharField(verbose_name="Ім'я", max_length=20, unique=True)
    last_name = models.CharField(max_length=20)
    anonym = models.CharField(max_length=20)
    email = models.EmailField(verbose_name='email', max_length=254, unique=True)
    adress = models.CharField(max_length=254, blank=True)
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)
    card_number = models.CharField(max_length=30, blank=True)
    language = models.CharField(
        max_length=6,
        choices=[('UKR', 'UKR'), ('ENG', 'ENG')]
    )
    sex = models.CharField(max_length=6,
        choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')])
    phone = PhoneNumberField(unique=True)
    data_birthday = models.DateField(verbose_name='Дата народження',default='2000-09-12')
    choice_city = models.CharField(max_length=30, blank=True)


