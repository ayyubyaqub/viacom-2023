# Generated by Django 3.2.5 on 2022-06-30 14:43

from django.db import migrations
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0011_alter_blog_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_page',
            name='content',
            field=djrichtextfield.models.RichTextField(blank=True, null=True),
        ),
    ]
