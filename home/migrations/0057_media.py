# Generated by Django 3.2.5 on 2022-06-08 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0056_auto_20220606_1429'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/images')),
                ('video', models.FileField(blank=True, null=True, upload_to='media/videos')),
                ('article_link', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
