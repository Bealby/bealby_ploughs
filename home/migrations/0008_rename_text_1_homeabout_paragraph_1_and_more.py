# Generated by Django 4.2.17 on 2025-01-09 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_remove_homearticles_text_1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homeabout',
            old_name='text_1',
            new_name='paragraph_1',
        ),
        migrations.RenameField(
            model_name='homeabout',
            old_name='text_2',
            new_name='paragraph_2',
        ),
    ]
