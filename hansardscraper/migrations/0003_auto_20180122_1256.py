# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-22 11:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hansardscraper', '0002_auto_20180122_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blockquote',
            name='debate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quotes', to='hansardscraper.Debate'),
        ),
        migrations.AlterField(
            model_name='blockquote',
            name='speaker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quotes', to='hansardscraper.Speaker'),
        ),
    ]
