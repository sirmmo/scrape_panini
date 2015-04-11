# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_collection_list'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collection',
            old_name='list',
            new_name='the_list',
        ),
    ]
