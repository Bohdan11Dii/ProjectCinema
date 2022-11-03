import datetime
import json

from django.apps import apps
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.db import transaction, IntegrityError
from django.forms import modelformset_factory, inlineformset_factory, formset_factory
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.dateparse import parse_datetime
from django.views.generic import CreateView

from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation

from user.models import ProjectUser
from .forms import *
from .models import *


#Tranlation language
def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect('/')
    return response


# News
def news(request):
    """Вивід всіх новин"""
    model = NewsAndPromotions.objects.filter(page_type=1)
    context = {'model': model}
    return render(request, 'administrator/new_and_action/news.html', context)


def create_news(request):
    """Створення новин"""
    gallery_model = ImagesTitle()
    gallery_query_set = gallery_model.__class__.objects.none()

    model = NewsAndPromotions.NEWS

    news = CreateNewsAndPromotions(request.POST or None, request.FILES or None)
    seo = SeoBlockForm(request.POST or None)
    formset = ImageInlineFormset(request.POST or None, request.FILES or None, queryset=gallery_query_set)
    if request.method == 'POST':
        if news.is_valid() and seo.is_valid() and formset.is_valid():
            news.save(commit=False)
            collection_image = gallery_model.__class__.objects.create(title=news.cleaned_data['title'])
            collection_image.save()

            for form in formset:
                if form.instance.image:
                    form.save(commit=False)
                    form.instance.collection_image = collection_image
                    form.save()
            news.instance.collection_image = collection_image
            news.instance.page_type = model
            seo.save()
            news.instance.seo = seo.instance
            news.save()
            return redirect('news')
    else:
        news = CreateNewsAndPromotions()
        seo = SeoBlockForm()
        formset = ImageInlineFormset()
    context = {
        'form': news,
        'seo': seo,
        'formset': formset,
    }
    return render(request, 'administrator/new_and_action/news_create.html', context=context)


def update_new(request, pk):
    """Редагування новини"""
    news_model = apps.get_model('administrator', 'NewsAndPromotions')
    collection_image = apps.get_model('administrator', 'ImagesTitle')

    news_object = get_object_or_404(news_model, pk=pk)
    collection_image_object = get_object_or_404(collection_image, pk=news_object.collection_image.pk)
    # news_object.collection_image
    collection_image_query_set = collection_image_object.images_set.all()

    news = CreateNewsAndPromotions(instance=news_object)
    seo = SeoBlockForm(instance=news_object.seo)
    formset = ImageInlineFormset(queryset=collection_image_query_set)

    if request.method == 'POST':
        news = CreateNewsAndPromotions(request.POST or None, request.FILES or None, instance=news_object)
        seo = SeoBlockForm(request.POST or None, instance=news_object.seo)
        formset = ImageInlineFormset(request.POST or None, request.FILES or None, queryset=collection_image_query_set)
        if news.is_valid() and seo.is_valid() and formset.is_valid():
            formset.save(commit=False)
            for i in formset.new_objects:
                i.collection_image = collection_image_object
                i.save()
            formset.save()
            seo.save()
            news.instance.seo = seo.instance
            news.save()
            messages.success(request, "Successful modification")
            return redirect('news')
    context = {
        'form': news,
        'seo': seo,
        'formset': formset,

    }
    return render(request,  'administrator/new_and_action/news_edit.html', context)


def delete(request, pk):
    """Видалення новини"""
    model = NewsAndPromotions.objects.get(id=pk)
    seo_model = SeoBlock.objects.get(id=model.seo.pk)
    collection_image_model = ImagesTitle.objects.get(id=model.collection_image.pk)

    model.delete()
    seo_model.delete()
    collection_image_model.delete()

    return redirect('/news')


# Action

def action(request):
    """Вивід всіх акцій"""
    model = NewsAndPromotions.objects.filter(page_type=0)
    context = {'model': model}
    return render(request, 'administrator/new_and_action/action.html', context)


def create_action(request):
    """Створення акції"""
    gallery_model = ImagesTitle()
    gallery_query_set = gallery_model.__class__.objects.none()

    model = NewsAndPromotions.ACTION

    news = CreateNewsAndPromotions(request.POST or None, request.FILES or None)
    seo = SeoBlockForm(request.POST or None)
    formset = ImageInlineFormset(request.POST or None, request.FILES or None, queryset=gallery_query_set)
    if request.method == 'POST':
        if news.is_valid() and seo.is_valid() and formset.is_valid():
            news.save(commit=False)
            collection_image = gallery_model.__class__.objects.create(title=news.cleaned_data['title'])
            collection_image.save()

            for form in formset:
                if form.instance.image:
                    form.save(commit=False)
                    form.instance.collection_image = collection_image
                    form.save()
            news.instance.collection_image = collection_image
            news.instance.page_type = model
            seo.save()
            news.instance.seo = seo.instance
            news.save()
            return redirect('action')
    else:
        news = CreateNewsAndPromotions()
        seo = SeoBlockForm()
        formset = ImageInlineFormset()
    context = {
        'form': news,
        'seo': seo,
        'formset': formset,
    }
    return render(request, 'administrator/new_and_action/action_create.html', context=context)


def update_action(request, pk):
    """Редагування акції"""
    news_model = apps.get_model('administrator', 'NewsAndPromotions')
    collection_image = apps.get_model('administrator', 'ImagesTitle')

    news_object = get_object_or_404(news_model, pk=pk)
    collection_image_object = get_object_or_404(collection_image, pk=news_object.collection_image.pk)
    collection_image_query_set = collection_image_object.images_set.all()

    news = CreateNewsAndPromotions(instance=news_object)
    seo = SeoBlockForm(instance=news_object.seo)
    formset = ImageInlineFormset(queryset=collection_image_query_set)

    if request.method == 'POST':
        news = CreateNewsAndPromotions(request.POST or None, request.FILES or None, instance=news_object)
        seo = SeoBlockForm(request.POST or None, instance=news_object.seo)
        formset = ImageInlineFormset(request.POST or None, request.FILES or None, queryset=collection_image_query_set)
        if news.is_valid() and seo.is_valid() and formset.is_valid():
            formset.save(commit=False)
            for i in formset.new_objects:
                i.collection_image = collection_image_object
                i.save()
            formset.save()
            seo.save()
            news.instance.seo = seo.instance
            news.save()
            messages.success(request, "Successful modification")
            return redirect('action')
    context = {
        'form': news,
        'seo': seo,
        'formset': formset,

    }
    return render(request,  'administrator/new_and_action/action_edit.html', context)


def delete_action(request, pk):
    """Видалення акції"""
    model = NewsAndPromotions.objects.get(id=pk)
    seo_model = SeoBlock.objects.get(id=model.seo.pk)
    collection_image_model = ImagesTitle.objects.get(id=model.collection_image.pk)

    model.delete()
    seo_model.delete()
    collection_image_model.delete()

    return redirect('/action')

# Film

def film(request):
    """Вивід всіх фільмів"""
    model_film = FilmModel()
    context = {}
    context['actual_film'] = model_film.__class__.objects.filter(is_active=0)
    context['show_film'] = model_film.__class__.objects.filter(is_active=1)
    return render(request, 'administrator/film/films.html', context)


def create_film_poster(request):
    """Створення фільмів"""
    gallery_model = ImagesTitle()
    gallery_query_set = gallery_model.__class__.objects.none()

    model = FilmModel.POSTER

    film = FilmForm(request.POST or None, request.FILES or None)
    seo = SeoBlockForm(request.POST or None)
    formset = ImageInlineFormset(request.POST or None, request.FILES or None, queryset=gallery_query_set)
    if request.method == 'POST':
        if film.is_valid() and seo.is_valid() and formset.is_valid():
            film.save(commit=False)
            collection_image = gallery_model.__class__.objects.create(title=film.cleaned_data['title'])
            collection_image.save()
            for form in formset:
                if form.instance.image:
                    form.save(commit=False)
                    form.instance.collection_image = collection_image
                    form.save()
            film.instance.collection_image = collection_image
            film.instance.is_active = model
            seo.save()
            film.instance.seo = seo.instance
            film.save()
            return redirect('film')
    else:
        film = FilmForm()
        seo = SeoBlockForm()
        formset = ImageInlineFormset()
    context = {
        'form': film,
        'seo': seo,
        'formset': formset,
    }
    return render(request, 'administrator/film/add_film.html', context=context)


def create_film_show(request):
    """Створення фільмів для скорого показу"""
    gallery_model = ImagesTitle()
    gallery_query_set = gallery_model.__class__.objects.none()

    model = FilmModel.InAWhile

    film = FilmForm(request.POST or None, request.FILES or None)
    seo = SeoBlockForm(request.POST or None)
    formset = ImageInlineFormset(request.POST or None, request.FILES or None, queryset=gallery_query_set)
    if request.method == 'POST':
        if film.is_valid() and seo.is_valid() and formset.is_valid():
            film.save(commit=False)
            collection_image = gallery_model.__class__.objects.create(title=film.cleaned_data['title'])
            collection_image.save()
            for form in formset:
                if form.instance.image:
                    form.save(commit=False)
                    form.instance.collection_image = collection_image
                    form.save()
            film.instance.collection_image = collection_image
            film.instance.is_active = model
            seo.save()
            film.instance.seo = seo.instance
            film.save()
            return redirect('film')
    else:
        film = FilmForm()
        seo = SeoBlockForm()
        formset = ImageInlineFormset()
    context = {
        'form': film,
        'seo': seo,
        'formset': formset,
    }
    return render(request, 'administrator/film/add_film.html', context=context)


def update_film(request, pk):
    """Редагування"""
    film_model = apps.get_model('administrator', 'FilmModel')
    collection_image = apps.get_model('administrator', 'ImagesTitle')

    film_object = get_object_or_404(film_model, pk=pk)
    collection_image_object = get_object_or_404(collection_image, pk=film_object.collection_image.pk)
    collection_image_query_set = collection_image_object.images_set.all()

    film_form = FilmForm(instance=film_object)
    seo = SeoBlockForm(instance=film_object.seo)
    formset = ImageInlineFormset(queryset=collection_image_query_set)

    if request.method == 'POST':
        film_form = FilmForm(request.POST or None, request.FILES or None, instance=film_object)
        seo = SeoBlockForm(request.POST or None, instance=film_object.seo)
        formset = ImageInlineFormset(request.POST or None, request.FILES or None, queryset=collection_image_query_set)
        if film_form.is_valid() and seo.is_valid() and formset.is_valid():
            formset.save(commit=False)
            for i in formset.new_objects:
                i.collection_image = collection_image_object
                i.save()
            formset.save()
            seo.save()
            film_form.instance.seo = seo.instance
            film_form.save()
            messages.success(request, "Successful modification")
            return redirect('film')
    context = {
        'form': film_form,
        'seo': seo,
        'formset': formset,

    }
    return render(request, 'administrator/film/update_film.html', context)


def delete_film(request, pk):
    """Видалення фільмів"""
    model = FilmModel.objects.get(id=pk)
    seo_model = SeoBlock.objects.get(id=model.seo.pk)
    collection_image_model = ImagesTitle.objects.get(id=model.collection_image.pk)

    model.delete()
    seo_model.delete()
    collection_image_model.delete()

    return redirect('/film')


# Cinema

def cinema(request):
    """Вивід всіх кінотеатрів"""
    cinema_model = CinemaModel.objects.all()
    context = {
        'model': cinema_model
    }
    return render(request, 'administrator/cinema_and_hall/cinema.html', context)


def create_cinema(request):
    """Створення кінотеатру"""
    collection_image_model = ImagesTitle()
    collection_image_set = collection_image_model.__class__.objects.none()

    cinema = CinemaForm(request.POST or None, request.FILES or None)
    seo = SeoBlockForm(request.POST or None)
    formset = ImageInlineFormset(request.POST or None, request.FILES or None, queryset=collection_image_set)
    if request.method == 'POST':
        if cinema.is_valid() and seo.is_valid() and formset.is_valid():
            cinema.save(commit=False)
            collection_image = collection_image_model.__class__.objects.create(title=cinema.cleaned_data['title'])
            collection_image.save()
            for form in formset:
                if form.instance.image:
                    form.save(commit=False)
                    form.instance.collection_image = collection_image
                    form.save()
            cinema.instance.collection_image = collection_image
            seo.save()
            cinema.instance.seo = seo.instance
            cinema.save()
            return redirect('cinema')
    else:
        cinema = CinemaForm()
        seo = SeoBlockForm()
        formset = ImageInlineFormset()
    context = {
        'form': cinema,
        'seo': seo,
        'formset': formset,
    }
    return render(request, 'administrator/cinema_and_hall/create_cinema.html', context=context)


def update_cinema(request, pk):
    """Редагування кінотеатру"""
    cinema_model = apps.get_model('administrator', 'CinemaModel')
    collection_image = apps.get_model('administrator', 'ImagesTitle')
    hall_model = apps.get_model('administrator', 'HallModel')

    cinema_object = get_object_or_404(cinema_model, pk=pk)
    collection_image_object = get_object_or_404(collection_image, pk=cinema_object.collection_image.pk)
    collection_image_query_set = collection_image_object.images_set.all()
    object_hall = hall_model.objects.filter(cinema=cinema_object)

    cinema_form = CinemaForm(instance=cinema_object)
    seo_form = SeoBlockForm(instance=cinema_object.seo)
    formset = ImageInlineFormset(queryset=collection_image_query_set)

    if request.method == "POST":
        cinema_form = CinemaForm(request.POST, request.FILES, instance = cinema_object)
        seo_form = SeoBlockForm(request.POST, instance=cinema_object.seo)
        formset = ImageInlineFormset(request.POST, request.FILES, queryset=collection_image_query_set)

        if cinema_form.is_valid() and seo_form.is_valid() and formset.is_valid():
            formset.save(commit=False)
            for i in formset.new_objects:
                i.collection_image = collection_image_object
                i.save()
            formset.save()
            seo_form.save()
            cinema_form.instance.seo = seo_form.instance
            cinema_form.save()
            messages.success(request, "Successful modification")
            return redirect('cinema')
    context = {
        'form': cinema_form,
        'seo': seo_form,
        'formset': formset,
        'hall': object_hall,
        'pk': pk
    }
    return render(request, 'administrator/cinema_and_hall/cinema_edit.html', context)


def delete_cinema(request, pk):
    """Видалення кінотеатру"""
    model = CinemaModel.objects.get(id=pk)
    seo_model = SeoBlock.objects.get(id=model.seo.pk)
    collection_image_model = ImagesTitle.objects.get(id=model.collection_image.pk)

    model.delete()
    seo_model.delete()
    collection_image_model.delete()

    return redirect('/cinema')


# Hall


def create_hall(request, pk):
    """Створення залу"""
    collection_image_model = ImagesTitle()
    collection_image_set = collection_image_model.__class__.objects.none()
    cinema = CinemaModel()

    hall_form = HallForm(request.POST or None, request.FILES or None)
    seo = SeoBlockForm(request.POST or None)
    formset = ImageInlineFormset(request.POST or None, request.FILES or None, queryset=collection_image_set)
    if request.method == 'POST':
        if hall_form.is_valid() and seo.is_valid() and formset.is_valid():
            hall_form.save(commit=False)
            model_cinema = cinema.__class__.objects.get(pk=pk)
            collection_image = collection_image_model.__class__.objects.create(title=hall_form.cleaned_data['title'])
            collection_image.save()
            for form in formset:
                if form.instance.image:
                    form.save(commit=False)
                    form.instance.collection_image = collection_image
                    form.save()
            hall_form.instance.collection_image = collection_image
            seo.save()
            hall_form.instance.seo = seo.instance
            hall_form.instance.cinema = model_cinema
            hall_form.save()
            return redirect('update_cinema', pk=pk)
    else:
        hall_form = HallForm()
        seo = SeoBlockForm()
        formset = ImageInlineFormset()
    context = {
        'form': hall_form,
        'seo': seo,
        'formset': formset,
        'pk': pk
    }
    return render(request, 'administrator/cinema_and_hall/create_hall.html', context)


def update_hall(request, pk):
    """Редагування залу"""
    hall_model = apps.get_model('administrator', 'HallModel')
    collection_image = apps.get_model('administrator', 'ImagesTitle')

    hall_object = get_object_or_404(hall_model, pk=pk)
    collection_image_object = get_object_or_404(collection_image, pk=hall_object.collection_image.pk)
    collection_image_query_set = collection_image_object.images_set.all()

    hall_form = HallForm(instance=hall_object)
    seo = SeoBlockForm(instance=hall_object.seo)
    formset = ImageInlineFormset(queryset=collection_image_query_set)

    if request.method == 'POST':
        hall_form = HallForm(request.POST or None, request.FILES or None, instance=hall_object)
        seo = SeoBlockForm(request.POST or None, instance=hall_object.seo)
        formset = ImageInlineFormset(request.POST or None, request.FILES or None, queryset=collection_image_query_set)
        if hall_form.is_valid() and seo.is_valid() and formset.is_valid():
            formset.save(commit=False)
            for i in formset.new_objects:
                i.collection_image = collection_image_object
                i.save()
            formset.save()
            seo.save()
            hall_form.instance.seo = seo.instance
            hall_form.save()
            messages.success(request, "Successful modification")
            return redirect('update_cinema', pk=hall_form.instance.cinema.pk)
    context = {
        'form': hall_form,
        'seo': seo,
        'formset': formset,
        'pk': hall_form.instance.cinema.pk

    }
    return render(request, 'administrator/cinema_and_hall/hall_edit.html', context)


def delete_hall(request, pk):
    """Видалення залу"""
    model = HallModel.objects.get(id=pk)
    seo_model = SeoBlock.objects.get(id=model.seo.pk)
    collection_image_model = ImagesTitle.objects.get(id=model.collection_image.pk)

    cinema_id = model.cinema.id
    seo_model.delete()
    collection_image_model.delete()
    model.delete()
    return redirect(f'/update_cinema/{cinema_id}')


#Main Page

def main_page(request):
    """Вивід головної сторінки"""
    model_main = MainPageModel()
    contact_page = ContactPageModel()
    model_main.title = 'Головна сторінка'
    context = {}
    context['model'], _ = model_main.__class__.objects.get_or_create(title='Главная страница')
    context['contact'], _ = contact_page.__class__.objects.get_or_create(title='Контакты')
    # context['title'] = 'Список сторінок'
    other_model = OtherPageModel.objects.all()
    context['other_model'] = other_model
    return render(request, 'administrator/pages/page_info.html', context)


def edit_main_page(request, pk):
    """Редагування головної сторінки"""
    main_model = apps.get_model('administrator', 'MainPageModel')

    main_object = get_object_or_404(main_model, pk=pk)

    main_form = MainPageForm(instance=main_object)
    seo = SeoBlockForm(instance=main_object.seo)

    if request.method == 'POST':
        main_form = MainPageForm(request.POST or None, request.FILES or None, instance=main_object)
        seo = SeoBlockForm(request.POST or None, instance=main_object.seo)
        if main_form.is_valid() and seo.is_valid():
            seo.save()
            main_form.instance.seo = seo.instance
            main_form.save()
            messages.success(request, f"Відредаговано головну сторінку")
            return redirect('info')
    context = {
        'form': main_form,
        'seo': seo,

    }
    return render(request, 'administrator/pages/create_main_page.html', context)


def create_page(request):
    collection_image_model = ImagesTitle()
    collection_image_set = collection_image_model.__class__.objects.none()

    other_page = OtherPageForm(request.POST or None, request.FILES or None)
    seo = SeoBlockForm(request.POST or None)
    formset = ImageInlineFormset(request.POST or None, request.FILES or None, queryset=collection_image_set)
    if request.method == 'POST':
        if other_page.is_valid() and seo.is_valid() and formset.is_valid():
            other_page.save(commit=False)
            collection_image = collection_image_model.__class__.objects.create(title=other_page.cleaned_data['title'])
            collection_image.save()
            for form in formset:
                if form.instance.image:
                    form.save(commit=False)
                    form.instance.collection_image = collection_image
                    form.save()
            other_page.instance.collection_image = collection_image
            seo.save()
            other_page.instance.seo = seo.instance
            other_page.save()
            return redirect('info')
    context = {
        'form': other_page,
        'seo': seo,
        'formset': formset,
    }
    return render(request, 'administrator/pages/create_other_page.html', context=context)


def edit_other_page(request, pk):
    """Редагування всі сторінок"""
    other_page = apps.get_model('administrator', 'OtherpageModel')
    collection_image = apps.get_model('administrator', 'ImagesTitle')

    other_object = get_object_or_404(other_page, pk=pk)
    collection_image_object = get_object_or_404(collection_image, pk=other_object.collection_image.pk)
    collection_image_query_set = collection_image_object.images_set.all()

    other_form = OtherPageForm(instance=other_object)
    seo = SeoBlockForm(instance=other_object.seo)
    formset = ImageInlineFormset(queryset=collection_image_query_set)

    if request.method == 'POST':
        other_form = OtherPageForm(request.POST or None, request.FILES or None, instance=other_object)
        seo = SeoBlockForm(request.POST or None, instance=other_object.seo)
        formset = ImageInlineFormset(request.POST or None, request.FILES or None, queryset=collection_image_query_set)
        if other_form.is_valid() and seo.is_valid() and formset.is_valid():
            formset.save(commit=False)
            for i in formset.new_objects:
                i.collection_image = collection_image_object
                i.save()
            formset.save()
            seo.save()
            other_form.instance.seo = seo.instance
            other_form.save()
            messages.success(request, f"Відредаговано {other_object.title}")
            return redirect('info')
    context = {
        'form': other_form,
        'seo': seo,
        'formset': formset,

    }
    return render(request, 'administrator/pages/edit_other_page.html', context)


def edit_contact_page(request, pk):
    """Редагування всі контактів"""
    contacts_page_model = apps.get_model('administrator', 'ContactPageModel')
    contact_model = apps.get_model('administrator', 'ContactModel')

    contact_query_set = contact_model.objects.all()
    contacts_page_object = contacts_page_model.objects.get(title='Контакты')
    # contacts_page_object = get_object_or_404(contacts_page_model, pk=pk)

    seo = SeoBlockForm(request.POST or None, instance=contacts_page_object.seo)
    contacts_page_form = ContactPageForm(request.POST or None, instance=contacts_page_object)
    formset = ContactFormset(request.POST or None, request.FILES or None, queryset=contact_query_set, prefix='contact')

    if request.method == 'POST':
        if seo.is_valid() and formset.is_valid() and contacts_page_form.is_valid():

            instances = formset.save(commit=False)
            for instance in instances:
                instance.contact_page = contacts_page_object
                instance.save()
            formset.save()

            seo.save()
            contacts_page_form.instance.seo = seo.instance
            contacts_page_form.save()
            return redirect('info')
    context = {
        'contacts_page_form': contacts_page_form,
        'seo': seo,
        'formset': formset,
    }
    return render(request, 'administrator/pages/contact.html', context)


def delete_page(request, pk):
    """Видалення сторінок"""
    model = OtherPageModel.objects.get(id=pk)
    seo_model = SeoBlock.objects.get(id=model.seo.pk)
    collection_image_model = ImagesTitle.objects.get(id=model.collection_image.pk)

    model.delete()
    seo_model.delete()
    collection_image_model.delete()

    return redirect('/info')


def banner(request):
    """Створення банерів та їх редагування"""
    back_banner_model = BackgroundBannerModel()
    banner_model = BannerModel()
    collection_image_model = ImagesTitle()

    back_banner_obj, _ = back_banner_model.__class__.objects.get_or_create()
    main_banner, _ = banner_model.__class__.objects.get_or_create(name=0)
    news_banner, _ = banner_model.__class__.objects.get_or_create(name=1)

    main_image, is_main_image = collection_image_model.__class__.objects.get_or_create(title='main_for_banner')
    news_image, is_news_image = collection_image_model.__class__.objects.get_or_create(title='news_for_banner')

    if main_banner.collection_image:
        main_banner_queryset = main_image.images_set.all()
    else:
        main_banner_queryset = collection_image_model.__class__.objects.none()

    if news_banner.collection_image:
        news_banner_queryset = news_image.images_set.all()
    else:
        news_banner_queryset = collection_image_model.__class__.objects.none()

    backg_banner_form = BackgroundBannerForm(request.POST or None, request.FILES or None, instance=back_banner_obj)
    main_banner_form = BannerForm(request.POST or None, request.FILES or None, instance=main_banner, prefix='main')
    news_banner_form = BannerForm(request.POST or None, request.FILES or None, instance=news_banner, prefix='news')

    main_banner_formset = MainBannerFormset(request.POST or None, request.FILES or None, queryset=main_banner_queryset,
                                            prefix='main')
    news_banner_formset = NewsBannerFormset(request.POST or None, request.FILES or None, queryset=news_banner_queryset,
                                            prefix='news')

    if request.method == 'POST':
        if 'back_banner_obj' in request.POST:
            if backg_banner_form.is_valid():
                backg_banner_form.save()
                return redirect('banner')

        if 'main_banner_form' in request.POST:
            if main_banner_form.is_valid() and main_banner_formset.is_valid():
                if is_main_image:
                    main_image.save()
                    for form in main_banner_formset:
                        if form.instance.image:
                            form.save(commit=False)
                            form.instance.collection_image = main_image
                            form.save()
                else:
                    main_banner_formset.save(commit=False)
                    for i in main_banner_formset.new_objects:
                        i.collection_image = main_image
                        i.save()
                    main_banner_formset.save()
                main_banner_form.instance.collection_image = main_image
                main_banner_form.save()
                return redirect('banner')

        if 'news_banner_form' in request.POST:
            if news_banner_form.is_valid() and news_banner_formset.is_valid():
                if is_news_image:
                    news_image.save()
                    for form in news_banner_formset:
                        if form.instance.image:
                            form.save(commit=False)
                            form.instance.collection_image = news_image
                            form.save()
                else:
                    news_banner_formset.save(commit=False)
                    for i in news_banner_formset.new_objects:
                        i.collection_image = news_image
                        i.save()
                    news_banner_formset.save()
                news_banner_form.instance.collection_image = news_image
                news_banner_form.save()
                return redirect('banner')
    context = {
        'bg_banner_form': backg_banner_form,
        'main_banner_form': main_banner_form,
        'news_banner_form': news_banner_form,
        'main_banner_formset': main_banner_formset,
        'news_banner_formset': news_banner_formset
    }
    return render(request, 'administrator/banner/banner.html', context)


def statistic(request):
    """Вивід даних у статистику"""
    model_user = ProjectUser()
    model_film = FilmModel()

    context = {}
    context['user'] = model_user.__class__.objects.count()

    context['FEMALE'] = model_user.__class__.objects.filter(sex='FEMALE').count()
    context['MALE'] = model_user.__class__.objects.filter(sex='MALE').count()

    context['Poster'] = model_film.__class__.objects.filter(is_active=0).count()
    context['While'] = model_film.__class__.objects.filter(is_active=1).count()

    context['data'] = json.dumps(
        [
            {
                'female':  context['FEMALE'],
                'male': context['MALE']
            }
        ]
    )

    context['film'] = json.dumps(
        [
            {
                'poster': context['Poster'],
                'while': context['While']
            }
        ]
    )

    print("context['film']", context['film'])
    return render(request, 'administrator/statistic/index.html', context)


def upload_file(request):
    """Завантаження файлів"""
    model_user = ProjectUser.objects.all()
    print("model_user", model_user.values("email"))
    model = SendMail.objects.all()
    form = SendMailForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    else:
        form = SendMailForm()
    context = {
        'form': form,
        'model': model,
        'users': model_user,
    }

    return render(request, 'administrator/send_email/send_email.html', context)


def get_users(request):

    return redirect('/newsletter')


def delete_email(request, pk):
    """Видалення файлів"""
    model = SendMail.objects.get(id=pk)
    model.delete()
    return redirect('/send_mail')