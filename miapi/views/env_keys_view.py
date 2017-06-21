from django.conf import settings
from django.http import JsonResponse
from rest_framework import viewsets


class EnvKeysView(viewsets.ViewSet):
    """

    """
    def get_env_keys(self, request):


        discogs_envs = {
            'key': settings.DISCOGSKEY,
            'secret': settings.DISCOGSSECRET
        }


        return JsonResponse(discogs_envs, safe=False)