from django.http import JsonResponse
from miapi.models import Release, TrackRelease, Track, Artist
from rest_framework import viewsets
import json

class SearchTrackView(viewsets.ViewSet):
    '''

    '''

    def get_release_with_track(self, request):
        '''
        Get a user release with a track that matches the search term

        Method arguments:
          request -- The full HTTP request object
        '''

        # Load the JSON string of the request body into a dict
        track_request = json.loads(request.body.decode())
        searched_title = track_request['trackTitle']

        release_search_results = [{'track_title': searched_title}]

        user_releases = Release.objects.filter(userreleases__user=request.user, userreleases__own=1)
        track_releases = TrackRelease.objects.filter(release__userreleases__user=request.user)
        tracks = Track.objects.filter(trackreleases__release__userreleases__user=request.user, title=searched_title)
        artists = Artist.objects.filter(tracks__trackreleases__release__userreleases__user=request.user)

        release_with_track = {}

        for user_album in user_releases:
            for track_release in track_releases:
                if user_album.id == track_release.release_id:
                    for track in tracks:
                        if track_release.track_id == track.id and track.title == searched_title:
                            for artist in artists:
                                if track.artist_id == artist.id:
                                    release_with_track = {
                                        'artist': artist.name,
                                        'title': user_album.title,
                                        'year': user_album.year,
                                        'image': user_album.image,
                                        'release_type': user_album.release_type.name,
                                        'track_position': track_release.position
                                    }
                            release_search_results.append(release_with_track)

        return JsonResponse(release_search_results, safe=False)