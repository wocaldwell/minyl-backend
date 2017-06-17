# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-14 20:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('miapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='release',
            name='release_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='releases', to='miapi.ReleaseType'),
        ),
        migrations.AlterField(
            model_name='userrelease',
            name='release',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userreleases', to='miapi.Release'),
        ),
    ]