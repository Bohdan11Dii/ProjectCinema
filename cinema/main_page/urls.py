from django.urls import path

from .views import index, logout_user, LoginView, RegisterUser, LoginUser

urlpatterns = [
    path('', index, name='home'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register', RegisterUser.as_view(), name='register'),
    # path('register', registration, name='register'),
]
