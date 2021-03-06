# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-16 01:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0007_auto_20180115_2333'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='create_date',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='create_date',
            new_name='created_date',
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
