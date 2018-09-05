# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-04 13:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180904_1341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='likes',
        ),
        migrations.AlterField(
            model_name='blog',
            name='bug',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bug_blog', to='bugs.Post'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='feature',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='feature_blog', to='features.Feature'),
        ),
    ]
