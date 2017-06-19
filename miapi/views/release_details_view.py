from django.http import JsonResponse
from miapi.models import *
from miapi.serializers import *
from django.core import serializers

from django.contrib.auth.models import User
from rest_framework.response import Response

from rest_framework import viewsets
import json

class ReleaseDetailsView(viewsets.ViewSet):
    """

    """
    def get_release_details(self, request):

        # Load the JSON string of the request body into a dict
        release_request = json.loads(request.body.decode())

        release = Release.objects.get(pk=release_request['release_id'])
        user_release = UserRelease.objects.get(user=request.user, release_id=release_request['release_id'])
        track_releases = TrackRelease.objects.filter(release__userreleases__user=request.user)
        tracks = Track.objects.filter(trackreleases__release__userreleases__user=request.user)
        artists = Artist.objects.filter(tracks__trackreleases__release__userreleases__user=request.user)
        tracklist = []
        for track_release in track_releases:
            if release.id == track_release.release_id:
                for track in tracks:
                    if track_release.track_id == track.id:
                        tracklist.append({
                            'track_title': track.title,
                            'track_position': track_release.position
                        })
                        for artist in artists:
                            if track.artist_id == artist.id:
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
        release_details['tracklist'] = tracklist

        # serialized_data = ReleaseSerializer(release, many=True, context={'request': request})
        # serialized_artists = ArtistSerializer(artists, many=True, context={'request': request})

        return JsonResponse(release_details, safe=False)
        # return JsonResponse(serialized_data.data, safe=False)









