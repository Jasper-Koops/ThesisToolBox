# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-28 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hansardscraper', '0005_auto_20180122_1519'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchQuery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
                ('finished', models.BooleanField(default=False)),
                ('quotes', models.ManyToManyField(blank=True, null=True, to='hansardscraper.BlockQuote')),
            ],
        ),
    ]
