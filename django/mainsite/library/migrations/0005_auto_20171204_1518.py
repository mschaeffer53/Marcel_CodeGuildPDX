# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 23:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_auto_20171204_1456'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rentalstatus',
            name='checked_in_out',
        ),
        migrations.AddField(
            model_name='rentalstatus',
            name='checked_in',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='rentalstatus',
            name='timestamp',
            field=models.DateField(default=datetime.datetime(2017, 12, 4, 23, 18, 34, 674497, tzinfo=utc)),
        ),
    ]
