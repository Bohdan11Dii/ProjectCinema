from django.urls import path

from .views import user, create_user

urlpatterns = [
    path('', user, name='user'),
    path('create_user/', create_user, name='create_user'),

]
