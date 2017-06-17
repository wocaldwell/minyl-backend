from django.http import HttpResponse
from miapi.models import Track
import json
from rest_framework import viewsets



class AddTrackView(viewsets.ViewSet):

    def add_track(self, request):
        '''Handles the creation of a new track

        Method arguments:
          request -- The full HTTP request object
        '''

        # Load the JSON string of the request body into a dict
        req_body = json.loads(request.body.decode())

        tracks = req_body['tracklist']

        tracks_ids = []

        for track in tracks:
            added_track = Track.objects.get_or_create(
                    title=track['title'],
                    artist_id=req_body['artist_id']
                )
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

