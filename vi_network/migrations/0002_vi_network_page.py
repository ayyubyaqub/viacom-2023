# Generated by Django 3.2.5 on 2022-06-26 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vi_network', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vi_Network_Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_keywords', models.TextField(default='')),
                ('meta_description', models.TextField(default='')),
                ('meta_title', models.TextField(default='')),
            ],
        ),
    ]
