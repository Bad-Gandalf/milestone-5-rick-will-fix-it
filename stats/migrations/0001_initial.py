# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-08 16:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bugs', '0009_auto_20180802_1147'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostWorkTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_spent_mins', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bugs.Post')),
            ],
        ),
    ]
