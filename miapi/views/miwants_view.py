from django.http import JsonResponse
from miapi.models import *
from miapi.serializers import *
from django.core import serializers

from django.contrib.auth.models import User
from rest_framework.response import Response

from rest_framework import viewsets

class MiWantsView(viewsets.ViewSet):
    """

    """
    def wants_list(self, request):

        user_releases = Release.objects.filter(userreleases__user=request.user, userreleases__own=0)
        track_releases = TrackRelease.objects.filter(release__userreleases__user=request.user)
        tracks = Track.objects.filter(trackreleases__release__userreleases__user=request.user)
        artists = Artist.objects.filter(tracks__trackreleases__release__userreleases__user=request.user)

        miwants_releases = []

        for user_album in user_releases:
            for track_release in track_releases:
                if user_album.id == track_release.release_id:
                    for track in tracks:
                        if track_release.track_id == track.id:
                            for artist in artists:
                                if track.artist_id == artist.id:
                                    release_dict = {
                                        'release_id': user_album.id,
                                        'image': user_album.image,
                                        'artist': artist.name,
                                        'title': user_album.title,
                                        'year': user_album.year,
                                        'release_type': user_album.release_type.name
                                    }
            miwants_releases.append(release_dict)

        # serialized_data = ReleaseSerializer(user_releases, many=True, context={'request': request})
        # serialized_artists = ArtistSerializer(artists, many=True, context={'request': request})

        return JsonResponse(miwants_releases, safe=False)
        # return JsonResponse(serialized_data.data, safe=False)