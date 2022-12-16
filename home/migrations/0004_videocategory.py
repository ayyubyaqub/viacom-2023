# Generated by Django 3.2.5 on 2022-01-08 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0009_auto_20220107_1844'),
        ('home', '0003_videoseeding'),
    ]

    operations = [
        migrations.CreateModel(
            name='Videocategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='about_us')),
                ('supercategory', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='about_us', to='categories.supercategory')),
            ],
        ),
    ]