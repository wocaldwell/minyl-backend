import os
from django.conf import settings
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

class ArriveDryEnvView(viewsets.ViewSet):
    """

    """
    permission_classes = (AllowAny)


    def get_arrivedry_keys(self, request):


        arrivedry_envs = {
            'firebaseurl': settings.FIREBASEURL,
            'weatherkey': settings.WEATHERKEY,
            'weatherref': settings.WEATHERREF,
            'googlekey': settings.GOOGLEKEY
        }

        print('the envs', arrivedry_envs['firebasekey'], "-----------------")

        return JsonResponse(arrivedry_envs, safe=False)