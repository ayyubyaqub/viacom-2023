# Generated by Django 3.2.5 on 2022-06-10 08:01

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0061_alter_two_four_seven_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='two_four_seven',
            name='content',
        ),
        migrations.AddField(
            model_name='two_four_seven',
            name='body',
            field=ckeditor.fields.RichTextField(default=''),
            preserve_default=False,
        ),
    ]
