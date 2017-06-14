from django.contrib.auth.models import User, Group
from rest_framework import serializers
from miapi.models import Release


class ReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Release
        exclude = ()


