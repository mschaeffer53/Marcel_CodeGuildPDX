# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 20:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_auto_20171204_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentalstatus',
            name='timestamp',
            field=models.DateField(default=datetime.datetime(2017, 12, 6, 20, 3, 27, 393835, tzinfo=utc)),
        ),
    ]
