# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-17 21:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corecluster', '0048_execution_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='mac',
            field=models.CharField(blank=True, default=b'', help_text=b'Mac address for node wakeup', max_length=30),
        ),
    ]