# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-19 16:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('year', models.CharField(max_length=4)),
                ('catalog_number', models.CharField(max_length=30)),
                ('label', models.CharField(max_length=128)),
                ('image', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='ReleaseType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='tracks', to='miapi.Artist')),
            ],
        ),
        migrations.CreateModel(
            name='TrackRelease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=8)),
                ('release', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='releasetracks', to='miapi.Release')),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='trackreleases', to='miapi.Track')),
            ],
        ),
        migrations.CreateModel(
            name='UserRelease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('own', models.IntegerField()),
                ('release', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='userreleases', to='miapi.Release')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='userreleases', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='release',
            name='release_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='releases', to='miapi.ReleaseType'),
        ),
    ]
