# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-28 15:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hansardscraper', '0008_auto_20180128_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queryparams',
            name='matches',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
