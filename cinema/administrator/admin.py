from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
# Register your models here.
from .models import *


@admin.register(NewsAndPromotions)
class NewsAndPromotionsTranslationAdmin(TranslationAdmin):
    pass


@admin.register(SeoBlock)
class SeoBlockTranslationAdmin(TranslationAdmin):
    pass


# @admin.register(Images)
# class ImagesTranslationAdmin(TranslationAdmin):
#     pass


@admin.register(FilmModel)
class FilmModelTranslationAdmin(TranslationAdmin):
    pass


@admin.register(CinemaModel)
class CinemaModelTranslationAdmin(TranslationAdmin):
    pass


@admin.register(HallModel)
class HallModelTranslationAdmin(TranslationAdmin):
    pass


@admin.register(MainPageModel)
class MainPageModelTranslationAdmin(TranslationAdmin):
    pass


@admin.register(OtherPageModel)
class OtherPageModelTranslationAdmin(TranslationAdmin):
    list_display = ('title', 'description')

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


# @admin.register(ContactPageModel)
# class ContactPageModelTranslationAdmin(TranslationAdmin):
#     pass
#
#
@admin.register(ContactModel)
class ContactModelTranslationAdmin(TranslationAdmin):
    pass

# @admin.register(ImagesTitle)
# class ImagesTitleTranslationAdmin(TranslationAdmin):
#     pass


admin.site.register(BannerModel)
admin.site.register(BackgroundBannerModel)
admin.site.register(ImagesTitle)
admin.site.register(ContactPageModel)
admin.site.register(SendMail)
