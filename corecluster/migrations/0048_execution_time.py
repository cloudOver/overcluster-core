# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-12 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corecluster', '0047_proxy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='execution_time',
            field=models.IntegerField(default=0, help_text=b'Total time in milliseconds spent on function execution time'),
        ),
    ]