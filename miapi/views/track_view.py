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
        print(req_body)
        print('------------------------')

        tracks = req_body['tracklist']
        print(len(tracks))
        for track in tracks:
            print('track is', track)
            added_track = Track.objects.get_or_create(
                    title=track['title'],
                    artist_id=req_body['artist_id']
                )
       # # Return the artist id to the client
       #  try:
       #      data = json.dumps({"artist_id":artist.id})
       #  except AttributeError:
       #      data = json.dumps({"artist_id":artist[0].id})
       #  return HttpResponse(data, content_type='application/json')

        return HttpResponse('track added to db!!!!!!!!!!!!!!!!!')
