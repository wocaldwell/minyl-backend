from django.http import HttpResponse
from miapi.models import Artist
import json
from rest_framework import viewsets



class AddArtistView(viewsets.ViewSet):

    def add_artist(self, request):
        '''Handles the creation of a new artist

        Method arguments:
          request -- The full HTTP request object
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

