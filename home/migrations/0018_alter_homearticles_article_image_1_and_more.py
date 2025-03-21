# Generated by Django 4.2.17 on 2025-01-14 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_alter_homeabout_about_image_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homearticles',
            name='article_image_1',
            field=models.ImageField(blank=True, help_text='Please upload images 600x400. Max 300px', null=True, upload_to='', verbose_name='(HOME) Article - Image 1'),
        ),
        migrations.AlterField(
            model_name='homearticles',
            name='article_image_1_description',
            field=models.CharField(blank=True, max_length=254, null=True, verbose_name='(HOME) Article - Image Description 1'),
        ),
        migrations.AlterField(
            model_name='homearticles',
            name='article_image_2',
            field=models.ImageField(blank=True, help_text='Please upload images 600x400. Max 300px', null=True, upload_to='', verbose_name='(HOME) Article - Image 2'),
        ),
        migrations.AlterField(
            model_name='homearticles',
            name='article_image_2_description',
            field=models.CharField(blank=True, max_length=254, null=True, verbose_name='Article - Image Description 2'),
        ),
        migrations.AlterField(
            model_name='homearticles',
            name='article_image_3',
            field=models.ImageField(blank=True, help_text='Please upload images 600x400. Max 300px', null=True, upload_to='', verbose_name='(HOME) Article - Image 3'),
        ),
        migrations.AlterField(
            model_name='homearticles',
            name='article_image_3_description',
            field=models.CharField(blank=True, max_length=254, null=True, verbose_name='Article - Image Description 3'),
        ),
        migrations.AlterField(
            model_name='homearticles',
            name='article_title_1',
            field=models.CharField(blank=True, max_length=254, null=True, verbose_name='(HOME) Article - Title 1'),
        ),
        migrations.AlterField(
            model_name='homearticles',
            name='article_title_2',
            field=models.CharField(blank=True, max_length=254, null=True, verbose_name='(HOME) Article - Title 2'),
        ),
        migrations.AlterField(
            model_name='homearticles',
            name='article_title_3',
            field=models.CharField(blank=True, max_length=254, null=True, verbose_name='(HOME) Article - Title 3'),
        ),
    ]
