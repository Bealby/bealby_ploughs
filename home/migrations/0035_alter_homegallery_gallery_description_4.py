# Generated by Django 5.1.5 on 2025-04-18 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0034_alter_homegallery_gallery_description_5_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homegallery',
            name='gallery_description_4',
            field=models.CharField(blank=True, max_length=254, null=True, verbose_name='4. Gallery - Description'),
        ),
    ]
