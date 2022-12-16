# Generated by Django 3.2.5 on 2022-06-10 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0058_marketing_marketing_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shorts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Shorts_Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=200)),
                ('paragraph', models.TextField()),
            ],
        ),
    ]
