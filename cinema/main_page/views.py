from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterUserForm
from .utils import DataMixin


# from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    return render(request, 'main_page/index.html')




def login(request):
    return HttpResponse('Авторизація')


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'main_page/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = 'Реєстрація')
        return dict(list(context.items()) + list(c_def.items()))