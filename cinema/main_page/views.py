from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from administrator.models import FilmModel, MainPageModel, BannerModel, Images, CinemaModel, NewsAndPromotions, \
    OtherPageModel, ContactModel, ContactPageModel
from user.models import ProjectUser
from .forms import CustomUserCreationForm, LoginUserForm


# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate


class RegisterUser(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'main_page/register.html'
    success_url = reverse_lazy('login')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main_page/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


def index(request):
    """Вивід головної сторінки"""
    model_film = FilmModel()
    model_page = MainPageModel()
    model_banner_news = BannerModel.objects.filter(name=1)
    model_banner_main = BannerModel.objects.filter(name=0)
    context = {}
    context['actual_film'] = model_film.__class__.objects.filter(is_active=0)
    context['show_film'] = model_film.__class__.objects.filter(is_active=1)
    context["model_page"] = model_page.__class__.objects.all()

    context['news_banner'] = model_banner_news
    context['main_banner'] = model_banner_main

    for item in model_banner_main:
       item = item.collection_image.images_set.all()
       context['item'] = item
    #
    for image in model_banner_news:
       images = image.collection_image.images_set.all()
       context['item_news'] = images

    print("context['news_banner']",  context['news_banner'])
    return render(request, 'main_page/index/index.html', context)


def poster(request):
    model_film = FilmModel()
    context = {}
    context['actual_film'] = model_film.__class__.objects.filter(is_active=0)
    return render(request, 'main_page/poster/poster.html', context)


def soon(request):
    model_film = FilmModel()
    context = {}
    context['show_film'] = model_film.__class__.objects.filter(is_active=1)
    return render(request, 'main_page/soon/soon.html', context)


def cinema_(request):
    model_cinema = CinemaModel.objects.all()
    context = {}
    context['cinemas'] = model_cinema

    # print("context['cinemas']", context['cinemas'])
    return render(request, 'main_page/cinema/cinema.html', context)


def action_(request):
    model_action = NewsAndPromotions.objects.filter(page_type=0)
    context = {}
    context['action'] = model_action

    print("context['action']", context['action'])
    return render(request, 'main_page/action/promotions.html', context)


def about_cinema_history(request):
    value_1 = OtherPageModel.objects.get(title_uk='Про кінотеатр')
    value_2 = OtherPageModel.objects.get(title_en='About the cinema')
    model_cinema_history = OtherPageModel.objects.get(title__in=(value_1, value_2))
    # model_cinema_history = OtherPageModel.objects.get()
    context = {}
    context['model_cinema_history'] = model_cinema_history
    context['model_cinema_history_images'] = model_cinema_history.collection_image.images_set.all()
    print("context['model_cinema_history']", model_cinema_history.description)
    return render(request, 'main_page/about_cinema___/about_cinema.html', context)


def cafe_bar(request):
    value_1 = OtherPageModel.objects.get(title_uk='Кафе-Бар')
    value_2 = OtherPageModel.objects.get(title_en='Cafe-Bar')
    model_cafe_bar = OtherPageModel.objects.get(title__in=(value_1, value_2))
    context = {}
    context['model_cafe_bar'] = model_cafe_bar
    context['model_cafe_bar_images'] = model_cafe_bar.collection_image.images_set.all()
    print("context['model_cafe_bar']", context['model_cafe_bar'])
    return render(request, 'main_page/cafe_bar/cafe_bar.html', context)


def news_page(request):
    model_news = NewsAndPromotions.objects.filter(page_type=1)
    context = {}
    context['news'] = model_news

    print("context['news']", context['news'])
    return render(request, 'main_page/news_page/news.html', context)

def vip_hall(request):
    value_1 = OtherPageModel.objects.get(title_uk='Vip-зал')
    value_2 = OtherPageModel.objects.get(title_en='Vip-room')
    model_vip_hall = OtherPageModel.objects.get(title__in=(value_1, value_2))
    context = {}
    context['model_vip_hall'] = model_vip_hall
    context['model_vip_hall_images'] = model_vip_hall.collection_image.images_set.all()

    return render(request, 'main_page/vip_hall/vip.html', context)


def childrean_room(request):
    value_1 = OtherPageModel.objects.get(title_uk='Дитяча кімната')
    value_2 = OtherPageModel.objects.get(title_en='Children room')
    model_childrean_room = OtherPageModel.objects.get(title__in=(value_1, value_2))
    context = {}
    context['childrean_room'] = model_childrean_room
    context['childrean_room_images'] = model_childrean_room.collection_image.images_set.all()

    return render(request, 'main_page/childrean_room/childrean_room.html', context)


def advertising_page(request):
    value_1 = OtherPageModel.objects.get(title_uk='Реклама')
    value_2 = OtherPageModel.objects.get(title_en='Advertising')
    advertising_page = OtherPageModel.objects.get(title__in=(value_1, value_2))
    context = {}
    context['advertising_page'] = advertising_page
    context['advertising_page_images'] = advertising_page.collection_image.images_set.all()

    return render(request, 'main_page/advertising_page/advertising.html', context)


def mobile_page(request):
    value_1 = OtherPageModel.objects.get(title_uk='Мобільний додаток')
    value_2 = OtherPageModel.objects.get(title_en='Mobile application')
    mobile_page = OtherPageModel.objects.get(title__in=(value_1, value_2))
    context = {}
    context['mobile_page'] = mobile_page
    context['mobile_page_images'] = mobile_page.collection_image.images_set.all()

    return render(request, 'main_page/mobile_page/mobile_app.html', context)


