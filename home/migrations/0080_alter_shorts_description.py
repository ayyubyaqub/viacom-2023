# Generated by Django 3.2.5 on 2022-06-26 06:45

from django.db import migrations
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0079_auto_20220624_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorts',
            name='description',
            field=djrichtextfield.models.RichTextField(),
        ),
    ]
