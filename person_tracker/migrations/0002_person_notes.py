# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-05 12:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
        ('person_tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='notes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='notes.Note'),
        ),
    ]
