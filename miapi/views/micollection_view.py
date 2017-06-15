from django.http import JsonResponse
from miapi.models import *
from miapi.serializers import *
from django.core import serializers

from django.contrib.auth.models import User
from rest_framework.response import Response

from rest_framework import viewsets

class CollectionView(viewsets.ViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def collection_list(self, request):

        user_releases = Release.objects.filter(userreleases__user=request.user, userreleases__own=1)
        track_releases = TrackRelease.objects.filter(release__userreleases__user=request.user)
        tracks = Track.objects.filter(trackreleases__release__userreleases__user=request.user)
        artists = Artist.objects.filter(tracks__trackreleases__release__userreleases__user=request.user)

        releases_with_artist = []

        for user_album in user_releases:
            for track_release in track_releases:
                if user_album.id == track_release.release_id:
                    for track in tracks:
                        if track_release.track_id == track.id:
                            for artist in artists:
                                if track.artist_id == artist.id:
                                    print(user_album.title, ' ', artist.name)
                                    release_dict = {
                                        'artist': artist.name,
                                        'title': user_album.title,
                                        'year': user_album.year,
                                        'release_type': user_album.release_type.name
                                    }
            releases_with_artist.append(release_dict)
        print(releases_with_artist)

        # serialized_data = ReleaseSerializer(user_releases, many=True, context={'request': request})
        # serialized_artists = ArtistSerializer(artists, many=True, context={'request': request})

        return JsonResponse(releases_with_artist, safe=False)
        # return JsonResponse(serialized_data.data, safe=False)









