# Generated by Django 3.2.5 on 2022-01-11 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0009_auto_20220107_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='image',
            field=models.ImageField(upload_to='category'),
        ),
    ]
