# Generated by Django 4.2.17 on 2025-01-09 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_rename_text_1_homeabout_paragraph_1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homeabout',
            old_name='paragraph_1',
            new_name='text_1',
        ),
        migrations.RenameField(
            model_name='homeabout',
            old_name='paragraph_2',
            new_name='text_2',
        ),
    ]
