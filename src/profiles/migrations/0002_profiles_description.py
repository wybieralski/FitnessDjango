# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-26 18:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='description',
            field=models.TextField(default='description default text'),
        ),
    ]
