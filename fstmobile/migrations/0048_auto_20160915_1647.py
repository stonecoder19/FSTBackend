# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fstmobile', '0047_auto_20160914_0441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 15, 16, 47, 52, 196566, tzinfo=utc), verbose_name=b'auto_now_add=true', editable=False),
        ),
        migrations.AlterField(
            model_name='news',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 15, 16, 47, 52, 190804, tzinfo=utc), verbose_name=b'auto_now_add=true', editable=False),
        ),
    ]
