# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 08:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0004_team_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='abbreviation',
            field=models.CharField(default='', max_length=3),
            preserve_default=False,
        ),
    ]
