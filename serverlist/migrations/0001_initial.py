# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 09:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('duration', models.IntegerField(default=0)),
                ('score', models.IntegerField(default=0)),
                ('ratio', models.IntegerField(default=100)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerTemp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('duration', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=200)),
                ('bot', models.BooleanField(default=False)),
                ('bot_level', models.CharField(max_length=200)),
                ('add_duration', models.IntegerField(default=0)),
                ('add_score', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=200)),
                ('map_name', models.CharField(max_length=200)),
                ('server_name', models.CharField(max_length=200)),
                ('game_name', models.CharField(default='Counter-Strike 1.6', max_length=200)),
                ('host', models.CharField(max_length=200)),
                ('num_players', models.IntegerField(default=0)),
                ('max_players', models.IntegerField(default=0)),
                ('num_humans', models.IntegerField(default=0)),
                ('num_bots', models.IntegerField(default=0)),
                ('folder', models.CharField(default='None', max_length=200)),
                ('environment', models.CharField(default='Windows', max_length=200)),
                ('password_protected', models.CharField(default='No', max_length=10)),
                ('vac_secured', models.NullBooleanField(default=False)),
                ('server_type', models.CharField(default='None', max_length=200)),
                ('protocol', models.IntegerField(default=0)),
                ('response_header', models.CharField(default='None', max_length=200)),
                ('mod', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='playertemp',
            name='server',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='serverlist.Server'),
        ),
    ]
