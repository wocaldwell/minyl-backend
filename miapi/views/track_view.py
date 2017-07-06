from django.http import HttpResponse
from miapi.models import Track
from rest_framework import viewsets
import json



class AddTrackView(viewsets.ViewSet):
    '''
    API endpoint that handles the creation of a track.
    '''

    def add_track(self, request):
        '''
        Handles the creation of a new track/

        Arguments:
        request -- The full HTTP request object.

        Returns:
        An Http response that includes a list with the unique ids of the tracks added.
        '''

        # Load the JSON string of the request body into a dict
        req_body = json.loads(request.body.decode())

        # Store the tracks from the request in a variable
        tracks = req_body['tracklist']

        # A list that will hold the track ids
        tracks_ids = []

        for track in tracks:
            added_track = Track.objects.get_or_create(
                    title=track['title'],
                    artist_id=req_body['artist_id']
                )
            # After track is added put it's id in the id list
            try:
                tracks_ids.append({
                    'track_id':added_track.id,
                    'position': track['position']
                })
            except AttributeError:
                tracks_ids.append({
                    'track_id':added_track[0].id,
                    'position': track['position']
                })

        # Return the tracks ids to the client
            data = json.dumps(tracks_ids)
        return HttpResponse(data, content_type='application/json')

