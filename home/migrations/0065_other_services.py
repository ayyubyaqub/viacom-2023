# Generated by Django 3.2.5 on 2022-06-10 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0064_auto_20220610_1353'),
    ]

    operations = [
        migrations.CreateModel(
            name='other_services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=250)),
                ('title', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='others')),
                ('description', models.TextField()),
            ],
        ),
    ]