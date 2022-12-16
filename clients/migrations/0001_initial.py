# Generated by Django 2.2.12 on 2021-12-28 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0004_categories_super_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=254)),
                ('client_logo', models.ImageField(upload_to='')),
                ('client_cover', models.ImageField(upload_to='')),
                ('client_videos', models.IntegerField()),
                ('client_shoots', models.IntegerField()),
                ('description', models.TextField()),
                ('super_category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='categories.SuperCategory')),
            ],
        ),
        migrations.CreateModel(
            name='ClientVideos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.Clients')),
            ],
        ),
    ]
