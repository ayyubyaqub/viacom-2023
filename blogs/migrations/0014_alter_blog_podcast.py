# Generated by Django 3.2.5 on 2022-07-04 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0013_auto_20220702_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='podcast',
            field=models.URLField(blank=True, null=True),
        ),
    ]
