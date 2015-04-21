# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0005_activity_language'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=20)),
                ('activity', models.ForeignKey(related_name='tags', to='lessons.Activity')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
