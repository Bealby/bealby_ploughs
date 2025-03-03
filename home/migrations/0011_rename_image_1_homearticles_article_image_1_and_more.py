# Generated by Django 4.2.17 on 2025-01-10 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_rename_text_1_homeabout_paragraph_1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homearticles',
            old_name='image_1',
            new_name='article_image_1',
        ),
        migrations.RenameField(
            model_name='homearticles',
            old_name='image_1_description',
            new_name='article_image_1_description',
        ),
        migrations.RenameField(
            model_name='homearticles',
            old_name='image_2',
            new_name='article_image_2',
        ),
        migrations.RenameField(
            model_name='homearticles',
            old_name='image_2_description',
            new_name='article_image_2_description',
        ),
        migrations.RenameField(
            model_name='homearticles',
            old_name='image_3',
            new_name='article_image_3',
        ),
        migrations.RenameField(
            model_name='homearticles',
            old_name='image_3_description',
            new_name='article_image_3_description',
        ),
        migrations.AddField(
            model_name='homearticles',
            name='article_title_1',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='homearticles',
            name='article_title_2',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='homearticles',
            name='article_title_3',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
