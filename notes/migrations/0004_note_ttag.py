# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-12 18:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='ttag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='notes.Tag'),
        ),
    ]