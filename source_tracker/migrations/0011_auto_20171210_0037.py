# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-09 23:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('source_tracker', '0010_auto_20171209_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='source',
            name='added_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
