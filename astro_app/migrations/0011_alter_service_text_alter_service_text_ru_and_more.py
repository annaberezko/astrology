# Generated by Django 4.0.4 on 2022-06-13 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astro_app', '0010_articles_keywords_ru_articles_keywords_uk_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='text',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='service',
            name='text_ru',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='text_uk',
            field=models.TextField(default='', null=True),
        ),
    ]
