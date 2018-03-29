# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mdfserver', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subpage',
            name='pages',
        ),
        migrations.DeleteModel(
            name='Page',
        ),
        migrations.DeleteModel(
            name='Subpage',
        ),
    ]
