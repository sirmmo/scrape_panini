# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_comic_contains'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comic',
            name='contains',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comic',
            name='notes',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
