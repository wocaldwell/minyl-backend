from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth.models import User
from miapi.models import *
from miapi.serializers import *
from rest_framework import viewsets
import json

class ReleaseDetailsView(viewsets.ViewSet):
    '''
    API endpoint that shows the details of a release.
    '''

    def get_release_details(self, request):
        '''
        Handles the compiling of the details for a requested release.

        Arguments:
        request -- The full HTTP request object.

        Returns:
        A Json response that includes the requested release details.
        '''

        # Load the JSON string of the request body into a dict
        release_request = json.loads(request.body.decode())

        # Get the requested release by id
        release = Release.objects.get(pk=release_request['release_id'])
        # Get the user release by id and user
        user_release = UserRelease.objects.get(user=request.user, release_id=release_request['release_id'])
        # Filter the release track join table by user release and user
        track_releases = TrackRelease.objects.filter(release__userreleases__user=request.user)
        # Filter the track table by track release, user release and user
        tracks = Track.objects.filter(trackreleases__release__userreleases__user=request.user)
        # Filter the artist table by tracks, track release, user release and user
        artists = Artist.objects.filter(tracks__trackreleases__release__userreleases__user=request.user)

        # List to store tracks on release
        tracklist = []

        for track_release in track_releases:
            if release.id == track_release.release_id:
                for track in tracks:
                    if track_release.track_id == track.id:
                        # add tracks to tracklist
                        tracklist.append({
                            'track_title': track.title,
                            'track_position': track_release.position
                        })
                        for artist in artists:
                            if track.artist_id == artist.id:
                                # compile information for requsted release
                                release_details = {
                                    'release_id': release.id,
                                    'image': release.image,
                                    'artist': artist.name,
                                    'title': release.title,
                                    'year': release.year,
                                    'release_type': release.release_type.name,
                                    'label': release.label,
                                    'catalog_number': release.catalog_number,
                                    'own_id': user_release.own
                                }

        # add the tracklist to the release details
        release_details['tracklist'] = tracklist

        return JsonResponse(release_details, safe=False)








