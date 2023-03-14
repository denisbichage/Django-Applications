# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-04 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dues',
            fields=[
                ('sid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('roomfees', models.FloatField(max_length=4)),
                ('messfees', models.FloatField(max_length=4)),
                ('securitymoney', models.FloatField(max_length=4)),
                ('submission_date', models.DateField(auto_now=True)),
                ('totaldue', models.FloatField(max_length=4)),
                ('fine', models.FloatField(max_length=4)),
            ],
        ),
    ]
