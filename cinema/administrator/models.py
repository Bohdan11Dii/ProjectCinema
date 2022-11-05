from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

from django.core import validators

from cinema.settings import MEDIA_URL
from user.models import ProjectUser


class ImagesTitle(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        db_table = 'images_title'


class Images(models.Model):
    collection_image = models.ForeignKey(ImagesTitle, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery/')
    url = models.URLField()
    text = models.CharField(max_length=50)

    class Meta:
        db_table = 'images'


class SeoBlock(models.Model):
    seo_url = models.URLField(max_length=200)
    seo_title = models.CharField(max_length=50)
    seo_keywords = models.CharField(max_length=50)
    seo_description = models.TextField()


class Meta:
        db_table = 'seo_block'


class NewsAndPromotions(models.Model):
    ACTION = 0
    NEWS = 1

    PAGE_TYPE = (
        (ACTION, 'Action'),
        (NEWS, 'News'),
    )

    is_published = models.BooleanField(default=False)
    title = models.CharField(max_length=50)
    data_published = models.DateTimeField(default=timezone.now)
    description = models.TextField(null=True, blank=True)
    images = models.ImageField(upload_to='images/')
    collection_image = models.ForeignKey(ImagesTitle,
                                         on_delete=models.CASCADE, null=True)
    link = models.URLField(max_length=200)
    seo = models.ForeignKey(SeoBlock,
                            on_delete=models.CASCADE, null=True)
    page_type = models.IntegerField(choices=PAGE_TYPE, default=ACTION)

    def __str__(self):
        return self.title

    USERNAME_FIELD = 'email'

    class Meta:
        db_table = 'news_and_promotions'


class FilmModel(models.Model):
    POSTER = 0
    InAWhile = 1

    SHOW_FILM = (
        (POSTER, 'Poster'),
        (InAWhile, 'while'),
    )
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    images = models.ImageField(upload_to='images/')
    collection_image = models.ForeignKey(ImagesTitle,
                                         on_delete=models.CASCADE, null=True)
    link = models.URLField(max_length=200)
    is_active = models.IntegerField(choices=SHOW_FILM, default=POSTER)
    type_of_film_3D = models.BooleanField(default=False)
    type_of_film_2D = models.BooleanField(default=False)
    type_of_film_IMAX = models.BooleanField(default=False)
    seo = models.ForeignKey(SeoBlock,
                            on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'film_page'


class CinemaModel(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    condition = models.TextField(null=True, blank=True)
    logo = models.ImageField(upload_to='logo/')
    banner = models.ImageField(upload_to='banner/')
    collection_image = models.ForeignKey(ImagesTitle,
                                         on_delete=models.CASCADE, null=True)
    seo = models.ForeignKey(SeoBlock,
                            on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'cinema_page'


class HallModel(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    sceme_hall = models.ImageField(upload_to='hall/')
    banner = models.ImageField(upload_to='banner/')
    collection_image = models.ForeignKey(ImagesTitle,
                                         on_delete=models.CASCADE, null=True)
    seo = models.ForeignKey(SeoBlock,
                            on_delete=models.CASCADE, null=True)
    cinema = models.ForeignKey(CinemaModel,
                               on_delete=models.CASCADE, null=True)
    data_published = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'hall_page'

class MainPageModel(models.Model):
    title = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)
    data_published = models.DateTimeField(default=timezone.now)
    phone_1 = PhoneNumberField()
    phone_2 = PhoneNumberField()
    seo_text = models.TextField(null=True, blank=True)
    seo = models.ForeignKey(SeoBlock,
                            on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'main_page'


class OtherPageModel(models.Model):
    data_published = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=False)
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    images = models.ImageField(upload_to='images/')
    collection_image = models.ForeignKey(ImagesTitle,
                                         on_delete=models.CASCADE, null=True)
    seo = models.ForeignKey(SeoBlock,
                            on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'other_page'


class ContactPageModel(models.Model):
    # CONTACT = 0
    #
    # CONTACTS = (
    #     (CONTACT, 'contacts'),
    # )
    # name = models.IntegerField(choices=CONTACTS, default=CONTACT)
    title = models.CharField(max_length=50)
    data_published = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    seo = models.ForeignKey(SeoBlock,
                            on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'contact_pages'


class ContactModel(models.Model):
    title = models.CharField(max_length=50)
    address = models.TextField(blank=True)
    coordinates = models.URLField(blank=True)
    is_active = models.BooleanField(default=False)
    logo = models.ImageField(upload_to='contact/')

    contact_page = models.ForeignKey(ContactPageModel, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'contact'


class BackgroundBannerModel(models.Model):
    choice_photo = models.CharField(max_length=20, choices=[('Фото на фоне', 'Фото на фоне'), ("Просто фон", "Просто фон")],
                            default="Просто фон")
    image = models.ImageField(upload_to='background/', null=True,
                              default=None)

    class Meta:
        db_table = 'back_banner'


class BannerModel(models.Model):
    MAIN = 0
    NEWS = 1

    SHOW = (
        (MAIN, 'main'),
        (NEWS, 'news'),
    )
    name = models.IntegerField(choices=SHOW, default=MAIN)
    collection_image = models.ForeignKey(ImagesTitle,
                                         on_delete=models.CASCADE, null=True)
    is_published = models.BooleanField(default=False)
    rotation_speed = models.IntegerField(null=True)

    class Meta:
        db_table = 'banner'


class SendMail(models.Model):
    file = models.FileField(upload_to='file/',
                            validators=[validators.FileExtensionValidator(['html'],
                            message='file повинун бути html файл')])
    choice_user = models.CharField(max_length=20, choices=[('Всі користувачі', 'Всі користувачі'), ("Вибрані", "Вибрані")],
                            default="Всі користувачі")
    data_published = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'send_mail'
