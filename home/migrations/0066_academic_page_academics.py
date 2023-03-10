# Generated by Django 3.2.5 on 2022-06-10 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0065_other_services'),
    ]

    operations = [
        migrations.CreateModel(
            name='Academic_page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=300)),
                ('image1', models.ImageField(upload_to='academic')),
                ('image2', models.ImageField(upload_to='academic')),
                ('image3', models.ImageField(upload_to='academic')),
            ],
        ),
        migrations.CreateModel(
            name='Academics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='academic')),
                ('description', models.TextField()),
                ('body', models.TextField()),
                ('duration', models.CharField(blank=True, max_length=200)),
                ('skill_field', models.CharField(blank=True, max_length=200)),
                ('slug', models.SlugField(editable=False)),
            ],
        ),
    ]
