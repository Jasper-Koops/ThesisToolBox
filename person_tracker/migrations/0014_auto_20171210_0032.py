# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-09 23:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person_tracker', '0013_auto_20171113_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='added_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
