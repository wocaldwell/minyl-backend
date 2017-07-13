from django.conf import settings
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from miapi.models import Quote


class QuoteView(viewsets.ViewSet):
    '''
    API endpoint that allows quotes accessed.
    '''

    'Custom permissions for this view only.'
    permission_classes = (AllowAny,)

    def get_quotes(self, request):
        '''
        Handles getting all of the rock quotes from database.

        Arguments:
        request -- The full HTTP request object.

        Returns:
        A Json response that includes the all of the quotes in the database.
        '''

        all_quotes = Quote.objects.all()


        return JsonResponse(all_quotes, safe=False)