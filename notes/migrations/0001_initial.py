# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-05 12:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
            ],
        ),
    ]
