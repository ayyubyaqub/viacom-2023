# Generated by Django 3.2.5 on 2022-06-11 05:47

from django.db import migrations
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0067_alter_academics_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academics',
            name='body',
            field=djrichtextfield.models.RichTextField(blank=True, null=True),
        ),
    ]
