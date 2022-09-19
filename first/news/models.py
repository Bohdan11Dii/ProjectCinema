from django.db import models
from django.utils import timezone


class ImagesTitle(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        db_table = 'images_title'


class Images(models.Model):
    collection_image = models.ForeignKey(ImagesTitle, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery/')

    class Meta:
        db_table = 'images'


class SeoBlock(models.Model):
    url = models.URLField(max_length=200)
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        db_table = 'seo_block'


class NewsAndPromotions(models.Model):
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

    def __str__(self):
        return self.title

    USERNAME_FIELD = 'email'

    class Meta:
        db_table = 'news_and_promotions'






