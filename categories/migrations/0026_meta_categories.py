# Generated by Django 3.2.5 on 2022-06-11 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0025_delete_metatags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meta_Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_name', models.CharField(default='', max_length=254)),
                ('meta_description', models.TextField(default='')),
                ('categories_parent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='categories.categories')),
            ],
        ),
    ]
