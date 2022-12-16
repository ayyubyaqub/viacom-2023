# Generated by Django 3.2.5 on 2022-01-28 18:52

import categories.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0010_alter_categories_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='image',
            field=models.ImageField(upload_to=categories.models.content_file_name),
        ),
        migrations.AlterField(
            model_name='categories',
            name='video',
            field=models.FileField(upload_to=categories.models.content_file_name),
        ),
    ]