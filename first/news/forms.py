import datetime
from django.forms import modelformset_factory, HiddenInput
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import NewsAndPromotions, SeoBlock, Images
from django.core import validators


class CreateNewsAndPromotions(forms.ModelForm):
    is_published = forms.BooleanField(required=False)
    data_published = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),
                                     initial=datetime.date.today(), localize=True)
    images = forms.ImageField(widget=forms.FileInput)

    class Meta:
        model = NewsAndPromotions
        exclude = ('seo', 'collection_image',)
        fields = '__all__'


class SeoBlockForm(forms.ModelForm):
    class Meta:
        model = SeoBlock
        fields = '__all__'


class ImagesForm(forms.ModelForm):
    images = forms.ImageField(required=False, widget=forms.FileInput, label='')

    class Meta:
        model = Images
        fields = ['images']


ImageInlineFormset = modelformset_factory(model=Images, form=ImagesForm,
                                          fields=('images',), extra=0, can_delete=True)
ImageInlineFormset.deletion_widget = HiddenInput



