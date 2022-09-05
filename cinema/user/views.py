from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import ProjectUser

from main_page.forms import CustomUserCreationForm


def user(request):
    users = ProjectUser.objects.all()
    context = {
        'users': users
    }
    return render(request, 'user/users.html', context)


def update_user(request, pk):
    id = ProjectUser.objects.get(id=pk)
    form = CustomUserCreationForm(instance=id)
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, instance=id)
        if form.is_valid():
            form.save()
            return redirect('/user')
    context = {'form': form}
    return render(request, 'user/create_user.html', context)


def delete_user(request, pk):
    id = ProjectUser.objects.get(id=pk)
    id.delete()
    return redirect('/user')





