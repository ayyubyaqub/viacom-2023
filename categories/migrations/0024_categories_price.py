# Generated by Django 4.0.2 on 2022-03-03 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0023_categories_landscapeimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
