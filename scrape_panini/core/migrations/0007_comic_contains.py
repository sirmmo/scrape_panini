# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20150308_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='comic',
            name='contains',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
