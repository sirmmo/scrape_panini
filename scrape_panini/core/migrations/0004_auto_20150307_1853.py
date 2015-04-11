# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_collection'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComicTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comic', models.ForeignKey(related_name='tagged_with', to='core.Comic')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='comictag',
            name='tag',
            field=models.ForeignKey(to='core.Tag'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='collection',
            name='comic',
            field=models.ForeignKey(related_name='owned_by', to='core.Comic'),
            preserve_default=True,
        ),
    ]
