# Generated by Django 3.2.1 on 2021-08-06 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0014_loggin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loggin',
            name='mobilenumber',
            field=models.IntegerField(max_length=50),
        ),
    ]
