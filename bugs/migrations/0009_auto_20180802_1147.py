# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-02 11:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bugs', '0008_comment_upvotes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='upvotes',
        ),
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(related_name='liked_post_comments', to=settings.AUTH_USER_MODEL),
        ),
    ]
