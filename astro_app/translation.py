from modeltranslation.translator import register, TranslationOptions
from astro_app.models import Articles, Pages, Reviews, Service


@register(Articles)
class ArticlesTranslationOptions(TranslationOptions):
    fields = ('name', 'keywords', 'text')


@register(Pages)
class PagesTranslationOptions(TranslationOptions):
    fields = ('title', 'name', 'keywords', 'description', 'text')


@register(Reviews)
class ReviewsTranslationOptions(TranslationOptions):
    fields = ('name', 'message')


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('name', 'short_text', 'text')
