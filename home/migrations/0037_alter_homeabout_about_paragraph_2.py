# Generated by Django 5.1.5 on 2025-06-01 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0036_alter_homeabout_about_paragraph_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeabout',
            name='about_paragraph_2',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='2. About - Paragraph '),
        ),
    ]
