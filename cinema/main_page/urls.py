from django.urls import path

from .views import index, login, RegisterUser

urlpatterns = [
    path('', index, name='home'),
    path('login/', login, name='login'),
    path('register', RegisterUser.as_view(), name='register'),
]
