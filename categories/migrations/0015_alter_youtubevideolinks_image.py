# Generated by Django 3.2.5 on 2022-02-02 12:04

import categories.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0014_rename_category_youtubevideolinks_super_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtubevideolinks',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=categories.models.content_file_name_video),
        ),
    ]
