# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-04 13:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='tasks',
            new_name='task',
        ),
    ]
