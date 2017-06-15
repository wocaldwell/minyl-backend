from django.contrib.auth.models import User, Group
from rest_framework import serializers
from miapi.models import *


class ReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Release
        exclude = ()

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        exclude = ()

class UserReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRelease
        exclude = ()


