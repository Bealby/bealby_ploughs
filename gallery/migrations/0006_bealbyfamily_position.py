# Generated by Django 5.1.5 on 2025-03-16 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_bealbyforestcart_bealbyplough_bealbyworkshop_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bealbyfamily',
            name='position',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
