from django.urls import path

from .views import news, create, update

urlpatterns = [
    path('news/', news, name='news'),
    path('create/', create, name='create'),
    path('update/<str:pk>/', update, name='update'),
    # path('delete/<str:pk>/', delete, name='delete'),

]
