from django.db import models
from django.contrib.auth.models import User


class ReleaseType(models.Model):
    name = models.CharField(max_length=25)

class Release(models.Model):
    title = models.CharField(max_length=300)
    release_type = models.ForeignKey(
      ReleaseType,
      on_delete=models.CASCADE
    )
    year = models.CharField(max_length=4)
    catalog_number = models.CharField(max_length=30)
    image = models.CharField(max_length=300)

class UserRelease(models.Model):
    user = models.ForeignKey(
      User,
      on_delete=models.CASCADE
    )
    release = models.ForeignKey(
      Release,
      on_delete=models.CASCADE
    )
    own = models.IntegerField()
