# Generated by Django 4.2.17 on 2025-01-15 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_homearticles_article_image_alt_text_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homearticles',
            name='article_image_alt_text_3',
            field=models.CharField(blank=True, help_text="'Alt' text required for image. Backend. Not seen on website", max_length=254, null=True, verbose_name='3. Image Description'),
        ),
        migrations.AlterField(
            model_name='homearticles',
            name='article_image_alt_text_2',
            field=models.CharField(blank=True, help_text="'Alt' text required for image. Backend. Not seen on website", max_length=254, null=True, verbose_name='2. Image Description'),
        ),
    ]
