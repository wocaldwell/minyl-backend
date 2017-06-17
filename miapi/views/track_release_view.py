from django.http import HttpResponse
from miapi.models import TrackRelease
import json
from rest_framework import viewsets

class AddTrackReleaseView(viewsets.ViewSet):

    def add_track_release(self, request):
        '''Handles the creation of a new track release

        Method arguments:
          request -- The full HTTP request object
        '''

        # Load the JSON string of the request body into a dict
        req_body = json.loads(request.body.decode())

        tracks_ids = req_body['tracksIds']


        for track in tracks_ids:
            added_track = TrackRelease.objects.get_or_create(
                    track_id=track['track_id'],
                    position=track['position'],
                    release_id=req_body['release_id']
                )
        return HttpResponse('you did it. . .')

