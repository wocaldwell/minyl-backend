from django.http import HttpResponse
from miapi.models import TrackRelease
from rest_framework import viewsets
import json

class AddTrackReleaseView(viewsets.ViewSet):
    '''
    API endpoint that allows for the addition of tracks to the track release join table.
    '''

    def add_track_release(self, request):
        '''
        Handles the creation of a new track release.

        Arguments:
        request -- The full HTTP request object.

        Returns:
        An Http response that includes a success status.
        '''

        # Load the JSON string of the request body into a dict
        req_body = json.loads(request.body.decode())

        # Store all track objects in a list
        tracks_ids = req_body['tracksIds']

        # For each track in the tracks list add an entry in the track release table
        for track in tracks_ids:
            added_track = TrackRelease.objects.get_or_create(
                    track_id=track['track_id'],
                    position=track['position'],
                    release_id=req_body['release_id']
                )

        return HttpResponse('you did it. . .', status=200)

