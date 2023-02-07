from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from administrator.models import FilmModel, MainPageModel, BannerModel, Images, CinemaModel, NewsAndPromotions, \
    OtherPageModel, ContactModel, ContactPageModel, BackgroundBannerModel, HallModel, SeanceModel

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


def base():
    model_background_model = BackgroundBannerModel()
    context = {}
    context['model_background_model'] = model_background_model.__class__.objects.all()

    for item in context['model_background_model']:
        context['back_image'] = item.image
        return context['back_image']


def index(request):
    """Вивід головної сторінки"""
    model_film = FilmModel()
    model_page = MainPageModel()
    model_banner_news = BannerModel.objects.filter(name=1)
    model_banner_main = BannerModel.objects.filter(name=0)
    model_background_model = BackgroundBannerModel()
    other_model = OtherPageModel.objects.all()

    context = {}

    context['model'] = other_model
    context['actual_film'] = model_film.__class__.objects.filter(is_active=0)
    context['show_film'] = model_film.__class__.objects.filter(is_active=1)
    context["model_page"] = model_page.__class__.objects.all()

    context['news_banner'] = model_banner_news
    context['main_banner'] = model_banner_main
    context['model_background_model'] = model_background_model.__class__.objects.all()

    
    for item in model_banner_main:
        if item is not None:
            pass
        else:
            item = item.collection_image.images_set.all()
            context['item'] = item
    #
    for image in model_banner_news:
        if image is not None:
            pass
        else:
            images = image.collection_image.images_set.all()
            context['item_news'] = images

    for item in context['model_background_model']:
        context['back_image'] = item.image

    return render(request, 'main_page/index/index.html', context)


def poster(request):
    model_film = FilmModel()
    other_model = OtherPageModel.objects.all()

    context = {}

    context['model'] = other_model
    context['actual_film'] = model_film.__class__.objects.filter(is_active=0)
    context['back_image'] = base()
    return render(request, 'main_page/poster/poster.html', context)


def soon(request):
    model_film = FilmModel()
    other_model = OtherPageModel.objects.all()

    context = {}

    context['model'] = other_model
    context['show_film'] = model_film.__class__.objects.filter(is_active=1)
    context['back_image'] = base()
    return render(request, 'main_page/soon/soon.html', context)


def cinema_(request):
    model_cinema = CinemaModel.objects.all()
    other_model = OtherPageModel.objects.all()

    context = {}

    context['model'] = other_model
    context['cinemas'] = model_cinema
    context['back_image'] = base()

    return render(request, 'main_page/cinema/cinema.html', context)


def action_(request):
    model_action = NewsAndPromotions.objects.filter(page_type=0)
    other_model = OtherPageModel.objects.all()

    context = {}

    context['model'] = other_model
    context['action'] = model_action
    context['back_image'] = base()

    return render(request, 'main_page/action/promotions.html', context)


def other_pages(request):
    other_model = OtherPageModel.objects.all()
    context = {
        'model': other_model
    }
    print()
    return render(request, 'main_page/base.html', context)


def news_page(request):
    model_news = NewsAndPromotions.objects.filter(page_type=1)
    other_model = OtherPageModel.objects.all()

    context = {}

    context['model'] = other_model
    context['news'] = model_news
    context['back_image'] = base()

    # print("context['news']", context['news'])
    return render(request, 'main_page/news_page/news.html', context)


def advertising_page(request, pk):
    other_model = OtherPageModel.objects.get(id=pk)
    model = OtherPageModel.objects.all()

    context = {}

    context['model'] = model
    context['back_image'] = base()
    context['model_other'] = other_model
    context['model_other_images'] = other_model.collection_image.images_set.all()
    # print("context['model_other']", context['model_other'])
    return render(request, 'main_page/advertising_page/advertising.html', context)


def contact_page(request):
    contact_page = ContactModel.objects.all()
    other_model = OtherPageModel.objects.all()

    context = {}

    context['model'] = other_model
    context['contact_page'] = contact_page
    context['back_image'] = base()

    # print("context['contact_page']", context['contact_page'])
    return render(request, 'main_page/contact_page/contact.html', context)


def get_action(request, pk):
    model_action = NewsAndPromotions.objects.get(id=pk)
    model_action_images = model_action.collection_image.images_set.all()
    other_model = OtherPageModel.objects.all()
    print("model_action", model_action)
    context = {
        "action": model_action,
        "back_image": base(),
        "images": model_action_images,
        "model": other_model
    }
    return render(request, 'main_page/action/card_promotions.html', context)


def get_cinema(request, pk):
    cinema_model = CinemaModel.objects.get(id=pk)
    hall_model = HallModel.objects.filter(cinema=pk)
    other_model = OtherPageModel.objects.all()

    model_cinema_images = cinema_model.collection_image.images_set.all()
    context = {
        "cinema": cinema_model,
        "back_image": base(),
        "images": model_cinema_images,
        'hall': hall_model.count(),
        'hall_model_': hall_model,
        "model": other_model
    }
    return render(request, 'main_page/cinema/cinema_card.html', context)


def get_hall(request, pk):
    hall_model = HallModel.objects.get(id=pk)
    other_model = OtherPageModel.objects.all()
    model_hall_images = hall_model.collection_image.images_set.all()
    context = {
        "hall": hall_model,
        "back_image": base(),
        "images": model_hall_images,
        "model": other_model

    }
    return render(request, 'main_page/cinema/hall_card.html', context)


def get_seance(request):
    seance_model = SeanceModel.objects.all()
    hall_model = HallModel.objects.all()
    film_model = FilmModel.objects.all()
    cinema_model = CinemaModel.objects.all()
    other_model = OtherPageModel.objects.all()
    
    context = {
        "seance": seance_model,
        "back_image": base(),
        "hall": hall_model,
        "film": film_model,
        "cinema": cinema_model,
        "model": other_model
    }
    return render(request, 'main_page/seance/seance.html', context)

def get_all(request, pk):
    
    return render(request, 'main_page/seance/seance_get.html')

def get_ticket(request, pk):
    ticket_model = FilmModel.objects.get(id=pk)
    print("TICKET", ticket_model.link)
    other_model = OtherPageModel.objects.all()
    context = {
        "back_image": base(),
        "film": ticket_model,
        "model": other_model
    }
    return render(request, 'main_page/seance/ticket.html', context)


