from django.urls import path

from .views import user, update_user, delete_user

urlpatterns = [
    path('', user, name='user'),
    # path('create_user/', create_user, name='create_user'),
    path('update_user/<str:pk>/', update_user, name='update_user'),
    path('delete_user/<str:pk>/', delete_user, name='delete_user'),

]
