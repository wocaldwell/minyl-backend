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

        new_artist = Artist(
            name=req_body['name'],
            )

        # Commit the release to the database by saving it
        new_artist.save()

        return HttpResponse('artist release added to db!!!!!!!!!!!!!!!!!')
