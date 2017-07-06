from django.conf import settings
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

class ArriveDryEnvView(viewsets.ViewSet, APIView):
    '''
    API endpoint that provides the arriveDry application credentials.
    '''

    'Custom permissions for this view only.'
    permission_classes = (AllowAny,)


    def get_arrivedry_keys():
        '''
        Get the external API keys for consumption by the ArriveDry application (another application that resides on server).

        Returns:
        A json response that has the API keys stored as environment variables.
        '''

        arrivedry_envs = {
            'firebaseurl': settings.FIREBASEURL,
            'weatherkey': settings.WEATHERKEY,
            'weatherref': settings.WEATHERREF,
            'googlekey': settings.GOOGLEKEY
        }


        return JsonResponse(arrivedry_envs, safe=False)