# Generated by Django 3.2.5 on 2022-02-05 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0018_alter_youtubevideolinks_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='supercategory',
            name='serial_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
