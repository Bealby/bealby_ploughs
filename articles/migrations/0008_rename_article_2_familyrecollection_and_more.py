# Generated by Django 5.1.5 on 2025-04-05 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_article_3'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Article_2',
            new_name='FamilyRecollection',
        ),
        migrations.RenameModel(
            old_name='Article_3',
            new_name='WorkshopAnecdote',
        ),
        migrations.AlterModelOptions(
            name='familyrecollection',
            options={'verbose_name_plural': 'Family Recollections'},
        ),
        migrations.AlterModelOptions(
            name='workshopanecdote',
            options={'verbose_name_plural': 'Workshop Anecdotes'},
        ),
    ]
