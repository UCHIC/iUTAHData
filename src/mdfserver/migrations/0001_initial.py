# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('content', models.TextField(max_length=20000)),
            ],
        ),
        migrations.CreateModel(
            name='Subpage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('url_visible', models.BooleanField()),
                ('content', models.TextField(max_length=20000)),
                ('pages', models.ForeignKey(to='mdfserver.Page')),
            ],
        ),
    ]
