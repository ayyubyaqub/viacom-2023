# Generated by Django 3.2.5 on 2022-06-10 08:07

from django.db import migrations
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0062_auto_20220610_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='two_four_seven',
            name='body',
            field=django_quill.fields.QuillField(),
        ),
    ]