# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-19 18:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('openpickr', '0008_auto_20170817_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='post_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
