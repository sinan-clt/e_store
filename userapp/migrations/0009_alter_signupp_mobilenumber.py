# Generated by Django 3.2.1 on 2021-08-06 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0008_auto_20210806_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signupp',
            name='mobilenumber',
            field=models.CharField(max_length=30),
        ),
    ]