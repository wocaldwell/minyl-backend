from django.http import JsonResponse
from miapi.models import Release, TrackRelease, Track, Artist
from rest_framework import viewsets
import json

class SearchTrackView(viewsets.ViewSet):
    '''
    API endpoint that compiles the release details for a searched track.
    '''

    def get_release_with_track(self, request):
        '''
        Get a user release with a track that matches the search term.

        Arguments:
        request -- The full HTTP request object.

        Returns:
        A Json response that includes a list of releases dictionaries and the track name dictionary
        '''

        # Load the JSON string of the request body into a dict
        track_request = json.loads(request.body.decode())

        # Set search term to a variable
        searched_title = track_request['trackTitle']

        # List that will store any database matches along with the searched track in an included dictionary
        release_search_results = [{'track_title': searched_title}]

        # Filter releases by user
        user_releases = Release.objects.filter(userreleases__user=request.user, userreleases__own=1)
        # Filter track releases by release and user
        track_releases = TrackRelease.objects.filter(release__userreleases__user=request.user)
        # Filter tracks by track release, release and user
        tracks = Track.objects.filter(trackreleases__release__userreleases__user=request.user, title=searched_title)
        # Filter artists by track, release and user
        artists = Artist.objects.filter(tracks__trackreleases__release__userreleases__user=request.user)

        # Dictionary to store release details
        release_with_track = {}

        for user_album in user_releases:
            for track_release in track_releases:
                if user_album.id == track_release.release_id:
                    for track in tracks:
                        if track_release.track_id == track.id and track.title == searched_title:
                            for artist in artists:
                                if track.artist_id == artist.id:
                                    # Conplile details for release
                                    release_with_track = {
                                        'artist': artist.name,
                                        'title': user_album.title,
                                        'year': user_album.year,
                                        'image': user_album.image,
                                        'release_type': user_album.release_type.name,
                                        'track_position': track_release.position
                                    }
                            # Add each release with searched track title to results list
                            release_search_results.append(release_with_track)

        return JsonResponse(release_search_results, safe=False)