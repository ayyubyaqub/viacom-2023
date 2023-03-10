# Generated by Django 3.2.5 on 2022-06-16 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('other_services', '0004_alter_other_services_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='other_services',
            name='yt_video_1',
        ),
        migrations.RemoveField(
            model_name='other_services',
            name='yt_video_2',
        ),
        migrations.RemoveField(
            model_name='other_services',
            name='yt_video_3',
        ),
        migrations.AddField(
            model_name='other_services',
            name='brief_youtube1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='other_services',
            name='brief_youtube2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='other_services',
            name='brief_youtube3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='other_services',
            name='image_youtube1',
            field=models.ImageField(blank=True, null=True, upload_to='othersvideoimage'),
        ),
        migrations.AddField(
            model_name='other_services',
            name='image_youtube2',
            field=models.ImageField(blank=True, null=True, upload_to='othersvideoimage'),
        ),
        migrations.AddField(
            model_name='other_services',
            name='image_youtube3',
            field=models.ImageField(blank=True, null=True, upload_to='othersvideoimage'),
        ),
        migrations.AddField(
            model_name='other_services',
            name='title_youtube1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='other_services',
            name='title_youtube2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='other_services',
            name='title_youtube3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='other_services',
            name='video_link_youtube1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='other_services',
            name='video_link_youtube2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='other_services',
            name='video_link_youtube3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='other_services',
            name='yt_heading',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
