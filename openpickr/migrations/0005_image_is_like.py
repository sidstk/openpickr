# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-12 05:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openpickr', '0004_remove_image_is_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='is_like',
            field=models.BooleanField(default=False),
        ),
    ]