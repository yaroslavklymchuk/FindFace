# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-05 06:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Signup', '0004_auto_20171030_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='joined_in',
            field=models.DateField(default=0),
            preserve_default=False,
        ),
    ]
