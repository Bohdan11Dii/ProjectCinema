import datetime
from django.forms import modelformset_factory, HiddenInput
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import NewsAndPromotions, SeoBlock, Images, FilmModel, CinemaModel, HallModel, OtherPageModel, \
    ContactPageModel, ContactModel, MainPageModel, BackgroundBannerModel, BannerModel
from django.core import validators
from phonenumber_field.formfields import PhoneNumberField


class CreateNewsAndPromotions(forms.ModelForm):
    is_published = forms.BooleanField(required=False)
    data_published = forms.DateField(widget=forms.DateInput(format='%Y-%m-%d',attrs={'type': 'date'}),
                                     initial=datetime.date.today(), localize=True,
                                     )
    images = forms.ImageField(widget=forms.FileInput, label="Головна картинка")

    class Meta:
        model = NewsAndPromotions
        exclude = ('seo', 'collection_image', 'page_type', )
        fields = '__all__'


class SeoBlockForm(forms.ModelForm):
    class Meta:
        model = SeoBlock
        fields = '__all__'


class ImagesForm(forms.ModelForm):
    image = forms.ImageField(required=False, widget=forms.FileInput, label='')

    class Meta:
        model = Images
        fields = ['image', 'text', 'url']


ImageInlineFormset = modelformset_factory(model=Images, form=ImagesForm,
                                          fields=('image',), extra=0, can_delete=True)
ImageInlineFormset.deletion_widget = HiddenInput


class FilmForm(forms.ModelForm):
    # images = forms.ImageField(widget=forms.FileInput, label="Головна картинка")
    type_of_film_3D = forms.BooleanField(required=False)
    type_of_film_2D = forms.BooleanField(required=False)
    type_of_film_IMAX = forms.BooleanField(required=False)

    class Meta:
        model = FilmModel
        exclude = ('seo', 'collection_image', 'is_active')
        fields = '__all__'


class CinemaForm(forms.ModelForm):
    # logo = forms.FileInput()
    # banner = forms.FileInput()
    class Meta:
        model = CinemaModel
        exclude = ('seo', 'collection_image',)
        fields = '__all__'


class HallForm(forms.ModelForm):
    class Meta:
        model = HallModel
        exclude = ('seo', 'collection_image', 'cinema', 'data_published')
        fields = '__all__'


class MainPageForm(forms.ModelForm):
    phone_1 = PhoneNumberField(widget=forms.TextInput(attrs={'class': 'phone-format', 'placeholder': "+380975647384"}))
    phone_2 = PhoneNumberField(widget=forms.TextInput(attrs={'class': 'phone-format', 'placeholder': "+380975647384"}))


    class Meta:
        model = MainPageModel
        exclude = ('seo', 'data_published', "title")
        fields = '__all__'


class OtherPageForm(forms.ModelForm):
    class Meta:
        model = OtherPageModel
        exclude = ('seo', 'data_published', "collection_image")
        fields = "__all__"


class ContactPageForm(forms.ModelForm):
    class Meta:
        model = ContactPageModel
        exclude = ('title', 'data_published', 'seo')
        fields = "__all__"


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        exclude = ('contact_page',)
        fields = "__all__"


ContactFormset = modelformset_factory(model=ContactModel, form=ContactForm,
                                      fields=('title', 'address', 'coordinates', 'is_active', 'logo'), extra=0,
                                      can_delete=True)
ContactFormset.deletion_widget = HiddenInput


class BackgroundBannerForm(forms.ModelForm):
    CHOICES = (('Фото на фоне', 'Фото на фоне'), ('Просто фон', 'Просто фон'),)
    choice_photo = forms.CharField(widget=forms.RadioSelect(choices=CHOICES, attrs={'class': 'form-input form_input checkbox_input'},))
    class Meta:
        model = BackgroundBannerModel
        fields = '__all__'


class BannerForm(forms.ModelForm):
    class Meta:
        model = BannerModel
        exclude = ('name', 'collection_image', )
        fields = '__all__'


MainBannerFormset = modelformset_factory(model=Images, form=ImagesForm, fields=('image', 'text', 'url'), extra=0, can_delete=True)
NewsBannerFormset = modelformset_factory(model=Images, form=ImagesForm, fields=('image', 'url'), extra=0, can_delete=True)

MainBannerFormset.deletion_widget = HiddenInput
NewsBannerFormset.deletion_widget = HiddenInput