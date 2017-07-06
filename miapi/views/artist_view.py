from django.http import HttpResponse
from miapi.models import Artist
from rest_framework import viewsets
import json



class AddArtistView(viewsets.ViewSet):
    '''
    API endpoint that allows artists to be added to the database.
    '''

    def add_artist(self, request):
        '''
        Handles the creation of a new artist.

        Arguments:
        request - The full HTTP request object.

        Returns:
        An Http request response that includes the unique id of the artist that was created.
        '''

        # Load the JSON string of the request body into a dict
        req_body = json.loads(request.body.decode())

        artist = Artist.objects.get_or_create(
            name=req_body['name'],
            )

        # Return the artist id to the client
        try:
            data = json.dumps({"artist_id":artist.id})
        except AttributeError:
            data = json.dumps({"artist_id":artist[0].id})

        return HttpResponse(data, content_type='application/json')

