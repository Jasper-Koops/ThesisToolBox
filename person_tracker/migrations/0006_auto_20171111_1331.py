# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-11 12:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person_tracker', '0005_auto_20171105_1352'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nationality',
            options={'verbose_name_plural': 'nationalities'},
        ),
    ]
