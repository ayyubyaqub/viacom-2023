# Generated by Django 3.2.5 on 2022-06-13 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dare2creative', '0003_rename_desciption_super_category_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='slug', editable=False),
            preserve_default=False,
        ),
    ]
