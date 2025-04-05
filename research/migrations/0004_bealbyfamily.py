# Generated by Django 5.1.5 on 2025-03-16 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0003_research_2'),
    ]

    operations = [
        migrations.CreateModel(
            name='BealbyFamily',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_header', models.CharField(blank=True, max_length=254, null=True, verbose_name='2. Image Title')),
                ('authur', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Title')),
                ('sub_header_1', models.CharField(blank=True, max_length=254, null=True, verbose_name='2. Image Title')),
                ('paragraph_1', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Text')),
                ('sub_header_2', models.CharField(blank=True, max_length=254, null=True, verbose_name='2. Image Title')),
                ('paragraph_2', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Text')),
                ('sub_header_3', models.CharField(blank=True, max_length=254, null=True, verbose_name='2. Image Title')),
                ('paragraph_3', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Text')),
            ],
            options={
                'verbose_name_plural': 'Bealby Family',
            },
        ),
    ]
