# Generated by Django 3.2.1 on 2021-08-06 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0005_auto_20210806_1632'),
    ]

    operations = [
        migrations.DeleteModel(
            name='loggin',
        ),
        migrations.DeleteModel(
            name='signupp',
        ),
    ]
