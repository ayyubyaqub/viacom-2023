# Generated by Django 3.2.5 on 2022-06-11 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0070_auto_20220611_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategories',
            name='keywords',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='subcategories',
            name='title',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='subcategories',
            name='description',
            field=models.TextField(default=''),
        ),
    ]