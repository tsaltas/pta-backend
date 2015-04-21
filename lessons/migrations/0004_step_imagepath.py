# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0003_activity_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='step',
            name='imagepath',
            field=models.ImageField(null=True, upload_to=b'step-images', blank=True),
            preserve_default=True,
        ),
    ]
