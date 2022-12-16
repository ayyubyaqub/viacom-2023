# Generated by Django 4.0.3 on 2022-04-13 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0050_rename_heading_black3_creators_heading_black_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(blank=True, max_length=254, null=True)),
                ('website', models.CharField(blank=True, max_length=254, null=True)),
                ('first_name', models.CharField(blank=True, max_length=254, null=True)),
                ('last_name', models.CharField(blank=True, max_length=254, null=True)),
                ('email', models.CharField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=254, null=True)),
                ('video_categories', models.CharField(blank=True, max_length=254, null=True)),
                ('other_project_details', models.CharField(blank=True, max_length=254, null=True)),
                ('project_description', models.CharField(blank=True, max_length=254, null=True)),
                ('project_country', models.CharField(blank=True, max_length=254, null=True)),
                ('project_city_state', models.CharField(blank=True, max_length=254, null=True)),
                ('project_pincode', models.CharField(blank=True, max_length=254, null=True)),
                ('delivery_speed', models.CharField(blank=True, max_length=254, null=True)),
                ('project_budget', models.CharField(blank=True, max_length=254, null=True)),
                ('reference_link', models.CharField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]
