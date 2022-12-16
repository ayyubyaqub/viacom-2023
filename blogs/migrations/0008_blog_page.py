# Generated by Django 3.2.5 on 2022-06-13 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0007_auto_20220613_1124'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=200)),
                ('others_heading', models.CharField(max_length=200)),
                ('shorts_heading', models.CharField(max_length=200)),
                ('meta_keywords', models.TextField(default='')),
                ('meta_description', models.TextField(default='')),
                ('meta_title', models.TextField(default='')),
            ],
        ),
    ]
