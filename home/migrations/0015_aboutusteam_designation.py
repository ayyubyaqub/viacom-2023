# Generated by Django 3.2.5 on 2022-01-25 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20220121_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutusteam',
            name='designation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
