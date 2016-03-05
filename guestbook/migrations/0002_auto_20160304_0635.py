# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestbook',
            name='createtime',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 4, 6, 35, 48, 939858)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='guestbook',
            name='email',
            field=models.EmailField(max_length=75, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='guestbook',
            name='reply',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='guestbook',
            name='replytime',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
    ]
