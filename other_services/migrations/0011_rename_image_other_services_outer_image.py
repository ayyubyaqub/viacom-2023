# Generated by Django 3.2.5 on 2022-06-25 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('other_services', '0010_auto_20220625_1521'),
    ]

    operations = [
        migrations.RenameField(
            model_name='other_services',
            old_name='image',
            new_name='outer_image',
        ),
    ]
