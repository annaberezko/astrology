# Generated by Django 4.0.4 on 2022-06-14 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astro_app', '0015_pages_description_pages_description_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pages',
            name='text',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='pages',
            name='text_ru',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='pages',
            name='text_uk',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
