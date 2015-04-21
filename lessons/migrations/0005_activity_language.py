# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0004_step_imagepath'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='language',
            field=models.CharField(default='Scratch', max_length=15),
            preserve_default=False,
        ),
    ]
