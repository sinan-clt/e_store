# Generated by Django 3.2.1 on 2021-08-06 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0015_alter_loggin_mobilenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loggin',
            name='mobilenumber',
            field=models.CharField(max_length=30),
        ),
    ]
