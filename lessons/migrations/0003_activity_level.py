# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0002_step_teachingnote'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='level',
            field=models.CharField(max_length=10, null=True, blank=True),
            preserve_default=True,
        ),
    ]
