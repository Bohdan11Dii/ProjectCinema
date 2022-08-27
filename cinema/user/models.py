from django.contrib.auth.models import AbstractBaseUser
from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField


class ProjectUser(models.Model):
    username = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    anonym = models.CharField(max_length=20)
    email = models.EmailField(max_length=254, unique=True)
    adress = models.CharField(max_length=254)
    password = models.CharField(max_length=20)
    card_number = models.CharField(max_length=30)
    language = models.BooleanField()
    sex = models.BooleanField()
    phone = models.CharField(max_length=13)
    birthday = models.DateField()
    choice_city = models.CharField(max_length=30)
    repeat_password = models.CharField(max_length=20)


    USERNAME_FIELD = 'email'