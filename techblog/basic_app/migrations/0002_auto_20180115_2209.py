# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-15 22:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 15, 22, 9, 22, 404728, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 15, 22, 9, 22, 403229, tzinfo=utc)),
        ),
    ]
