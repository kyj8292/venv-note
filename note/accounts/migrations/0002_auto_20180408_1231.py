# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-08 12:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='db',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]