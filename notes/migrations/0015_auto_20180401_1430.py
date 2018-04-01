# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-01 12:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notes', '0014_auto_20171217_1511'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thesis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='note',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]