# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-23 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corecluster', '0044_lease_hostname'),
    ]

    operations = [
        migrations.AddField(
            model_name='vm',
            name='websocket_enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vm',
            name='websocket_port',
            field=models.IntegerField(default=80),
        ),
    ]