# Generated by Django 3.2.5 on 2022-06-25 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('other_services', '0011_rename_image_other_services_outer_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='other_services',
            name='inner_image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='others/inner_images'),
        ),
    ]
