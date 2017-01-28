# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-15 16:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='home_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='scoreboard.Team'),
        ),
        migrations.AddField(
            model_name='game',
            name='visiting_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='scoreboard.Team'),
        ),
    ]
