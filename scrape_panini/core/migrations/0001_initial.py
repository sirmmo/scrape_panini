# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField()),
                ('cover', models.URLField()),
                ('price', models.FloatField()),
                ('brand', models.CharField(max_length=100)),
                ('ident', models.CharField(max_length=100)),
                ('notes', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
