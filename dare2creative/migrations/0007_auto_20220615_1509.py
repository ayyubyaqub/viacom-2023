# Generated by Django 3.2.5 on 2022-06-15 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dare2creative', '0006_auto_20220613_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='sub_category',
            name='company',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='sub_category',
            name='feautred',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sub_category',
            name='prize_money',
            field=models.IntegerField(default=0),
        ),
    ]