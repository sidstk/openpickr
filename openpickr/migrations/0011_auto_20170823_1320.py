# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 13:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openpickr', '0010_auto_20170822_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
