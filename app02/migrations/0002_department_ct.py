# Generated by Django 4.2.2 on 2023-06-13 02:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app02', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='ct',
            field=models.DateTimeField(default=datetime.date(2023, 6, 13), verbose_name='创建时间'),
        ),
    ]