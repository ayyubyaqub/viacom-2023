# Generated by Django 3.2.5 on 2022-06-24 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0078_auto_20220623_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='create_video',
            name='meta_description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='create_video',
            name='meta_keywords',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='create_video',
            name='meta_title',
            field=models.TextField(default=''),
        ),
    ]