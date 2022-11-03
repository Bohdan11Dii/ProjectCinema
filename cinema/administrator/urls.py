from django.urls import path

from .views import *

urlpatterns = [
    path('news/', news, name='news'),
    path('create_news/', create_news, name='create_news'),
    path('update_new/<str:pk>/', update_new, name='update_new'),
    path('delete/<str:pk>/', delete, name='delete'),

    path('action', action, name='action'),
    path('create_action/', create_action, name='create_action'),
    path('update_action/<str:pk>/', update_action, name='update_action'),
    path('delete_action/<str:pk>/', delete_action, name='delete_action'),

    path('film/', film, name='film'),
    path('create_film_poster/', create_film_poster, name='create_film'),
    path('create_film_show/', create_film_show, name='create_film_show'),
    path('update_film/<str:pk>/', update_film, name='update_film'),
    path('delete_film/<str:pk>/', delete_film, name='delete_film'),

    path('cinema/', cinema, name='cinema'),
    path('create_cinema/', create_cinema, name='create_cinema'),
    path('create_hall/<str:pk>/', create_hall, name='create_hall'),
    path('delete_cinema/<str:pk>/', delete_cinema, name='delete_cinema'),
    path('update_cinema/<str:pk>/', update_cinema, name='update_cinema'),
    path('update_hall/<str:pk>/', update_hall, name='update_hall'),
    path('delete_hall/<str:pk>/', delete_hall, name='delete_hall'),

    path('info/', main_page, name="info"),
    path('edit_main_page/<str:pk>/', edit_main_page, name="edit_main_page"),
    path('add_page', create_page, name="add_page"),
    path('delete_page/<str:pk>/', delete_page, name='delete_page'),
    path('edit_other_page/<str:pk>/', edit_other_page, name='edit_other_page'),
    path('edit_contact_page/<str:pk>/', edit_contact_page, name='edit_contact_page'),

    path('banner/', banner, name='banner'),
    path('statistic/', statistic, name='statistic'),

    path('send_mail/', upload_file, name='upload_file'),
    path('delete_email/<str:pk>/', delete_email, name='delete_email'),
    path('get_users/', get_users, name='get_users'),
]
