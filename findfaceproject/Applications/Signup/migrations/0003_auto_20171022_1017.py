# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-22 10:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Signup', '0002_subscribers_password'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subscribers',
            new_name='Subscriber',
        ),
    ]
