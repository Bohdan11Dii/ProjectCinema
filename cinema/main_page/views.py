from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from user.models import ProjectUser
from .forms import CustomUserCreationForm, LoginUserForm


# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate

def index(request):
    return render(request, 'main_page/index.html')


class RegisterUser(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'main_page/register.html'
    success_url = reverse_lazy('login')



class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main_page/login.html'

    # def get_context_data(self,*, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     c_def = self.get_user_context(title = 'Авторизація')
    #     return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')



#
# class LoginView(LoginView):
#     template_name = 'main_page/login.html'
#     def get(self, request, *args, **kwargs):
#         if self.request.user.is_authenticated:
#             return reverse_lazy('home')
#         return self.render_to_response(self.get_context_data())




def logout_user(request):
    logout(request)
    return redirect('login')