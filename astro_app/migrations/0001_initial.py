# Generated by Django 4.1.7 on 2023-03-17 14:17

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('name_ru', models.CharField(max_length=40, null=True)),
                ('name_uk', models.CharField(max_length=40, null=True)),
                ('keywords', models.CharField(default='', max_length=260)),
                ('keywords_ru', models.CharField(default='', max_length=260, null=True)),
                ('keywords_uk', models.CharField(default='', max_length=260, null=True)),
                ('description', models.CharField(blank=True, default='', max_length=260)),
                ('text', ckeditor.fields.RichTextField()),
                ('text_ru', ckeditor.fields.RichTextField(null=True)),
                ('text_uk', ckeditor.fields.RichTextField(null=True)),
                ('slug', models.SlugField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('title_ru', models.CharField(max_length=20, null=True)),
                ('title_uk', models.CharField(max_length=20, null=True)),
                ('name', models.CharField(max_length=20)),
                ('name_ru', models.CharField(max_length=20, null=True)),
                ('name_uk', models.CharField(max_length=20, null=True)),
                ('keywords', models.CharField(blank=True, default='', max_length=260)),
                ('keywords_ru', models.CharField(blank=True, default='', max_length=260, null=True)),
                ('keywords_uk', models.CharField(blank=True, default='', max_length=260, null=True)),
                ('description', models.CharField(blank=True, default='', max_length=260)),
                ('description_ru', models.CharField(blank=True, default='', max_length=260, null=True)),
                ('description_uk', models.CharField(blank=True, default='', max_length=260, null=True)),
                ('text', ckeditor.fields.RichTextField(blank=True, default='')),
                ('text_ru', ckeditor.fields.RichTextField(blank=True, default='', null=True)),
                ('text_uk', ckeditor.fields.RichTextField(blank=True, default='', null=True)),
                ('img_name', models.CharField(blank=True, default='', max_length=30)),
                ('slug', models.SlugField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('name_ru', models.CharField(max_length=30, null=True)),
                ('name_uk', models.CharField(max_length=30, null=True)),
                ('email', models.CharField(max_length=40)),
                ('message', models.TextField()),
                ('message_ru', models.TextField(null=True)),
                ('message_uk', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('name_ru', models.CharField(max_length=40, null=True)),
                ('name_uk', models.CharField(max_length=40, null=True)),
                ('short_text', models.CharField(max_length=400)),
                ('short_text_ru', models.CharField(max_length=400, null=True)),
                ('short_text_uk', models.CharField(max_length=400, null=True)),
                ('keywords', models.CharField(blank=True, default='', max_length=260)),
                ('description', models.CharField(blank=True, default='', max_length=260)),
                ('text', ckeditor.fields.RichTextField(blank=True, default='')),
                ('text_ru', ckeditor.fields.RichTextField(blank=True, default='', null=True)),
                ('text_uk', ckeditor.fields.RichTextField(blank=True, default='', null=True)),
                ('slug', models.SlugField(default='')),
            ],
        ),
    ]
