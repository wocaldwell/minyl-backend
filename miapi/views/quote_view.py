from django.conf import settings
from django.http import JsonResponse
from django.core import serializers
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
        # list that will store quotes and authors
        quotes_and_authors = []

        # get all values from Quote table
        all_quotes = Quote.objects.values()


        for quote in all_quotes:
            # add a quote and autor dictionary to quotes_and_authors list
            quotes_and_authors.append({
                'quote': quote['quote'],
                'author': quote['author']
                })

        # send the list of quotes and authors to the client as a json
        return JsonResponse(quotes_and_authors, safe=False)