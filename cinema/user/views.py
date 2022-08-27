from django.http import HttpResponse
from django.shortcuts import render
from .models import ProjectUser


def user(request):

    return render(request, 'user/users.html', {'title': 'Користувачі'})


def create_user(request):
    return render(request, 'user/create_user.html', {'title': 'Редагування користувачів'})