# Generated by Django 3.2.1 on 2021-08-06 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0013_delete_loggin'),
    ]

    operations = [
        migrations.CreateModel(
            name='loggin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobilenumber', models.IntegerField()),
                ('password', models.CharField(max_length=30)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.signupp')),
            ],
        ),
    ]
