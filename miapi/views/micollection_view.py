from django.http import JsonResponse
from miapi.models import *
from miapi.serializers import ReleaseSerializer
from django.core import serializers

def get_user_collection(request):
    '''Get all the releases a user owns.

    Method arguments:
      request -- The full HTTP request object
    '''
    user_releases = UserRelease.objects.filter(user=request.user, own=1)
    print(user_releases.value())
    data = Release.objects.all()
    print(data)
    serialized_data = ReleaseSerializer(data, many=True, context={'request': request})
    print(serialized_data)

    return JsonResponse(serialized_data.data, safe=False)








