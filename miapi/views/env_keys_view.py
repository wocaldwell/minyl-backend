from django.conf import settings
from django.http import JsonResponse
from rest_framework import viewsets


class EnvKeysView(viewsets.ViewSet):
    '''
    API endpoint that allows external API keys to be accessed.
    '''

    def get_env_keys(self, request):
        '''
        Handles setting of external API keys in a dictionary for consuption by the frontend.

        Arguments:
        request -- The full HTTP request object.

        Returns:
        A Json response that includes the API credentials.
        '''

        discogs_envs = {
            'key': settings.DISCOGSKEY,
            'secret': settings.DISCOGSSECRET
        }


        return JsonResponse(discogs_envs, safe=False)