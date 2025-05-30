# Generated by Django 4.2.17 on 2025-01-16 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_rename_article_article_2_alter_article_2_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='article_2',
            name='article_image',
            field=models.ImageField(blank=True, help_text='Please upload images 600x400. Max 300px', null=True, upload_to='', verbose_name='Image'),
        ),
        migrations.AddField(
            model_name='article_2',
            name='article_image_description',
            field=models.CharField(blank=True, help_text="'Alt' text required for image. Backend. Not seen on website", max_length=254, null=True, verbose_name='Image Description'),
        ),
        migrations.AddField(
            model_name='article_2',
            name='author',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Author'),
        ),
        migrations.AddField(
            model_name='article_2',
            name='text',
            field=models.CharField(blank=True, max_length=254, null=True, verbose_name='Workshop Anecdote Text'),
        ),
        migrations.AlterField(
            model_name='article_2',
            name='title',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Title'),
        ),
    ]
