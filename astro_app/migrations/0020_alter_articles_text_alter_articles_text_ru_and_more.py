# Generated by Django 4.0.4 on 2022-06-17 08:49

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('astro_app', '0019_articles_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='text',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='articles',
            name='text_ru',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='articles',
            name='text_uk',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
