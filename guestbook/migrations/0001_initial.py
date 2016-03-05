# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guestbook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nickname', models.CharField(max_length=16, unique=True)),
                ('email', models.EmailField(max_length=75, blank=True)),
                ('face', models.IntegerField()),
                ('content', models.TextField()),
                ('createtime', models.IntegerField(default=0)),
                ('clientip', models.CharField(max_length=15)),
                ('reply', models.TextField()),
                ('replytime', models.IntegerField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
