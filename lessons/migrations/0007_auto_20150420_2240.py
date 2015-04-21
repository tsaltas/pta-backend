# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0006_tag'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'verbose_name_plural': 'Activities'},
        ),
        migrations.AddField(
            model_name='activity',
            name='votecount',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
