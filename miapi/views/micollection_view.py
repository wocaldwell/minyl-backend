from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth.models import User
from miapi.models import *
from miapi.serializers import *
from rest_framework import viewsets

class CollectionView(viewsets.ViewSet):
    '''
    API endpoint that allows a user to see only the releases in their collection.
    '''
    def collection_list(self, request):
        '''
        Handles the filtering of the database tables to reveal only a users releases.

        Arguments:
        request -- The full HTTP request object.

        Returns:
        A Json response that includes the list of releases that the user has in their collection.
        '''

        # Filter the user releases table for this user
        user_releases = Release.objects.filter(userreleases__user=request.user, userreleases__own=1)
        # Filter the release tracks join table by this user and release
        track_releases = TrackRelease.objects.filter(release__userreleases__user=request.user)
        # Filter the tracks table by this user, release and release tracks
        tracks = Track.objects.filter(trackreleases__release__userreleases__user=request.user)
        # Filter the artists table by this user, release and release tracks and tracks
        artists = Artist.objects.filter(tracks__trackreleases__release__userreleases__user=request.user)

        # list that will store release and artist information for release in user collection
        releases_with_artist = []

        for user_album in user_releases:
            for track_release in track_releases:
                if user_album.id == track_release.release_id:
                    for track in tracks:
                        if track_release.track_id == track.id:
                            for artist in artists:
                                if track.artist_id == artist.id:
                                    # store each release details
                                    release_dict = {
                                        'release_id': user_album.id,
                                        'artist': artist.name,
                                        'title': user_album.title,
                                        'year': user_album.year,
                                        'release_type': user_album.release_type.name
                                    }
            # add release to the list
            releases_with_artist.append(release_dict)

        return JsonResponse(releases_with_artist, safe=False)









