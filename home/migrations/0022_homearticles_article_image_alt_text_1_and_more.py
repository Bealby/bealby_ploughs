# Generated by Django 4.2.17 on 2025-01-15 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_remove_homearticles_article_image_1_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homearticles',
            name='article_image_alt_text_1',
            field=models.CharField(blank=True, help_text="'Alt' text required for image. Backend. Not seen on website", max_length=254, null=True, verbose_name='1. Image Description'),
        ),
        migrations.AddField(
            model_name='homearticles',
            name='article_image_alt_text_2',
            field=models.CharField(blank=True, help_text="'Alt' text required for image. Backend. Not seen on website", max_length=254, null=True, verbose_name='3. Image Description'),
        ),
    ]
