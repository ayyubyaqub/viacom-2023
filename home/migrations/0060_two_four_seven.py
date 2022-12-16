# Generated by Django 3.2.5 on 2022-06-10 07:42

from django.db import migrations, models
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0059_shorts_shorts_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='Two_Four_Seven',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='24x7')),
                ('content', django_quill.fields.QuillField()),
            ],
        ),
    ]
