# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-10 06:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openpickr', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='comment',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]