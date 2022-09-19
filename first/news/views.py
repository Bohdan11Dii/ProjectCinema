import datetime

from django.apps import apps
from django.core.files.storage import FileSystemStorage
from django.db import transaction, IntegrityError
from django.forms import modelformset_factory, inlineformset_factory, formset_factory
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.dateparse import parse_datetime
from django.views.generic import CreateView

from .forms import CreateNewsAndPromotions, SeoBlockForm, ImagesForm, ImageInlineFormset
from .models import NewsAndPromotions, Images, SeoBlock, ImagesTitle


# Imaginary function to handle an uploaded file.

# Create your views here.

def news(request):
    """Вивід всіх новин"""
    model = NewsAndPromotions.objects.all()
    context = {'model': model}
    return render(request, 'news/news.html', context)


def create(request):
    """Створення новин"""
    gallery_model = apps.get_model('news', 'ImagesTitle')
    gallery_query_set = gallery_model.objects.none()

    cinema = CreateNewsAndPromotions(request.POST or None, request.FILES or None)
    seo = SeoBlockForm(request.POST or None)
    formset = ImageInlineFormset(request.POST or None, request.FILES or None, queryset=gallery_query_set)

    if request.method == 'POST':
        if cinema.is_valid() and seo.is_valid() and formset.is_valid():
            cinema.save(commit=False)
            collection_image = gallery_model.objects.create(title=cinema.cleaned_data['title'])
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
            return redirect('news')
    else:
        cinema = CreateNewsAndPromotions()
        seo = SeoBlockForm()
        formset = ImageInlineFormset()
    context = {
        'form': cinema,
        'seo': seo,
        'formset': formset,
    }
    return render(request, 'news/page_news.html', context=context)


def update(request, pk):
    """Редагування"""
    id_model = get_object_or_404(NewsAndPromotions, pk=pk)
    collection_object = get_object_or_404(ImagesTitle, pk=id_model.collection_image.pk)
    collection_object_query_set = collection_object.__class__.objects.all()
    # id_seo = SeoBlock.objects.get(id=pk)
    # id_images = ImagesTitle.objects.get(id=pk)

    form_new = CreateNewsAndPromotions(instance=id_model)
    seo_form = SeoBlockForm(instance=id_model.seo)
    formset = ImageInlineFormset(queryset=collection_object_query_set)
    if request.method == "POST":
        form_new = CreateNewsAndPromotions(request.POST, request.FILES, instance=id_model)
        seo_form = SeoBlockForm(request.POST, instance=id_model.seo)
        formset = ImageInlineFormset(request.POST, request.FILES, queryset=collection_object_query_set)
        if form_new.is_valid() and seo_form.is_valid() and formset.is_valid():
            formset.save(commit=False)
            for i in formset.new_objects:
                i.collection_image = collection_object
                i.save()
            for i in formset.changed_objects:
                i[0].save()
            seo_form.save()
            form_new.instance.seo = seo_form.instance
            form_new.save()
            return redirect('/news')
    context = {'form_new': form_new, 'seo_form': seo_form, 'formset': formset}
    return render(request,  'news/news_edit.html', context)



# def update(request, pk):
#     """Редагування"""
#     id_model = NewsAndPromotions.objects.get(id=pk)
#     form = CreateNewsAndPromotions(instance=id_model)
#     if request.method == "POST":
#         form = CreateNewsAndPromotions(request.POST, request.FILES, instance=id_model)
#         if form.is_valid():
#             form.save()
#             return redirect('/news')
#     context = {'form': form}
#     return render(request,  'news/page_news.html', context)
