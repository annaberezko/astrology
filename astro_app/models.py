from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from transliterate import translit
from ckeditor.fields import RichTextField


def latin_name(i):
    return translit(i, language_code='ru', reversed=True)


class Articles(models.Model):
    name = models.CharField(max_length=40)
    keywords = models.CharField(max_length=260, default='', null=False)
    description = models.CharField(max_length=260, default='', null=False, blank=True)
    text = RichTextField()
    slug = models.SlugField(default='', null=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(latin_name(self.name))
        super(Articles, self).save(*args, **kwargs)

    def get_url(self):
        return reverse("article_detail", args=[self.slug])

    def __str__(self):
        return f"{self.name} "


class Pages(models.Model):
    title = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    keywords = models.CharField(max_length=260, default='', null=False, blank=True)
    description = models.CharField(max_length=260, default='', null=False, blank=True)
    text = RichTextField(default='', null=False, blank=True)
    img_name = models.CharField(max_length=30, default='', null=False, blank=True)
    slug = models.SlugField(default='', null=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(latin_name(self.name))
        super(Pages, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"


class Reviews(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} "


class Service(models.Model):
    name = models.CharField(max_length=40)
    short_text = models.CharField(max_length=400)
    keywords = models.CharField(max_length=260, default='', null=False, blank=True)
    description = models.CharField(max_length=260, default='', null=False, blank=True)
    text = RichTextField(default='', null=False, blank=True)
    slug = models.SlugField(default='', null=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(latin_name(self.name))
        super(Service, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
