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


    def get_arrivedry_keys(self, request):
        '''

        '''

        arrivedry_envs = {
            'firebaseurl': settings.FIREBASEURL,
            'weatherkey': settings.WEATHERKEY,
            'weatherref': settings.WEATHERREF,
            'googlekey': settings.GOOGLEKEY
        }


        return JsonResponse(arrivedry_envs, safe=False)