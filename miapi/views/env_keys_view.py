import os
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
import json

class EnvKeysView(viewsets.ViewSet):
    """

    """
    def get_env_keys(self, request):


        discogs_envs = {
            'key': os.environ['DISCOGSKEY'],
            'secret': os.environ['DISCOGSSECRET']
        }

        print('the envs', os.environ['DISCOGSKEY'])

        return JsonResponse(discogs_envs, safe=False)