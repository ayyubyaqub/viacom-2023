# Generated by Django 3.2.5 on 2022-02-03 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0016_alter_youtubevideolinks_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtubevideolinks',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Inspired with our video'),
        ),
    ]
