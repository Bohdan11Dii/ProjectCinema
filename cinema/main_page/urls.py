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
    path('about_cinema_history', about_cinema_history, name='about_cinema_history'),
    path('cafe_bar', cafe_bar, name='cafe_bar'),
    path('news_page', news_page, name='news_page'),
    path('vip_hall', vip_hall, name='vip_hall'),
    path('childrean_room', childrean_room, name='childrean_room'),
    path('advertising_page', advertising_page, name='advertising_page'),
    path('mobile_page', mobile_page, name='mobile_page'),
]
