from django.contrib import admin
from astro_app.models import Articles, Pages, Reviews, Service


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ['name', 'name_uk']


@admin.register(Pages)
class PagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'name', 'name_uk']


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'name_uk']
