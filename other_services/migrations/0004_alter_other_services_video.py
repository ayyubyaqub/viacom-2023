# Generated by Django 3.2.5 on 2022-06-16 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('other_services', '0003_auto_20220616_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='other_services',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='others/videos'),
        ),
    ]
