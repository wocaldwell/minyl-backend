from django.db import models
from django.contrib.auth.models import User


class ReleaseType(models.Model):
    name = models.CharField(max_length=25)

class Release(models.Model):
    title = models.CharField(max_length=300)
    release_type = models.ForeignKey(
      ReleaseType,
      on_delete=models.CASCADE,
      related_name='releases'
    )
    year = models.CharField(max_length=4)
    catalog_number = models.CharField(max_length=30)
    label = models.CharField(max_length=128)
    image = models.CharField(max_length=512)

class UserRelease(models.Model):
    user = models.ForeignKey(
      User,
      on_delete=models.DO_NOTHING,
      related_name='userreleases'
    )
    release = models.ForeignKey(
      Release,
      on_delete=models.DO_NOTHING,
      related_name='userreleases'
    )
    own = models.IntegerField()

class Artist(models.Model):
    name = models.CharField(max_length=64)

class Track(models.Model):
    artist = models.ForeignKey(
        Artist,
        on_delete=models.DO_NOTHING,
        related_name='tracks'
    )
    title = models.CharField(max_length=128)

class TrackRelease(models.Model):
    track = models.ForeignKey(
        Track,
        on_delete=models.DO_NOTHING,
        related_name='trackreleases'
    )
    release = models.ForeignKey(
        Release,
        on_delete=models.DO_NOTHING,
        related_name='releasetracks'
    )
    position = models.CharField(max_length=8)
