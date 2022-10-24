from modeltranslation.translator import register, TranslationOptions
from .models import *


# @register(Images)
# class ImagesTranslationOptions(TranslationOptions):
#     fields = ('text', )


# @register(ImagesTitle)
# class ImagesTitleTranslationOptions(TranslationOptions):
#     fields = ('title',)


# @register(SeoBlock)
# class SeoBlockTranslationOptions(TranslationOptions):
#     fields = ('seo_title', 'seo_keywords', 'seo_description')


@register(NewsAndPromotions)
class NewsAndPromotionsTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )


@register(FilmModel)
class FilmModelTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(CinemaModel)
class CinemaModelTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'condition')


@register(HallModel)
class HallModelTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(MainPageModel)
class MainPageModelTranslationOptions(TranslationOptions):
    fields = ('seo_text', )


@register(OtherPageModel)
class OtherPageModelTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(ContactModel)
class ContactModelTranslationOptions(TranslationOptions):
    fields = ('title', 'address', 'coordinates')


