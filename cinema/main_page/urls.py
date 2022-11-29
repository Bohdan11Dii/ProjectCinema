from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register', RegisterUser.as_view(), name='register'),
    path('index', index, name='index'),
    path('poster', poster, name='poster'),
    path('soon', soon, name='soon'),
    path('cinema_', cinema_, name='cinema_'),
    path('action_', action_, name='action_'),

    path('news_page', news_page, name='news_page'),
    path('page/<str:pk>/', advertising_page, name='page'),
    path('contact_page', contact_page, name='contact_page'),

    path('other_pages', other_pages, name='other_pages'),

    path('get_action/<str:pk>/', get_action, name='get_action'),
    path('get_cinema/<str:pk>/', get_cinema, name='get_cinema'),
    path('get_hall/<str:pk>/', get_hall, name='get_hall'),
    path('get_seance', get_seance, name='get_seance'),
    path('get_ticket/<str:pk>/', get_ticket, name='get_ticket'),
    
    path('get_all/<str:pk>/', get_all, name='get_all'),

]