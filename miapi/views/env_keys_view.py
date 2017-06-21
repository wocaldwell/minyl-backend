import os
from django.conf import settings
# from settings import DISCOGSKEY, DISCOGSSECRET
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
import json

class EnvKeysView(viewsets.ViewSet):
    """

    """
    def get_env_keys(self, request):


        discogs_envs = {
            'key': settings.DISCOGSKEY,
            'secret': settings.DISCOGSSECRET
        }

        print('the envs', discogs_envs['key'], "-----------------")

        return JsonResponse(discogs_envs, safe=False)