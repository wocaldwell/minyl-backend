from django.http import HttpResponse
from miapi.models import UserRelease
import json
from rest_framework import viewsets



class AddUserReleaseView(viewsets.ViewSet):
    '''
    API endpiont that for adding a new user release.
    '''

    def add_user_release(self, request):
        '''
        Handles the creation of a new user release relationship.

        Arguments:
        request -- The full HTTP request object.

        Returns:
        An Http response that includes the new user release id.
        '''

        # Load the JSON string of the request body into a dict
        req_body = json.loads(request.body.decode())

        # Get or create a release with the request details
        new_user_release = UserRelease.objects.get_or_create(
            user=request.user,
            release_id=req_body['release_id'],
            own=req_body['own'],
            )

        # Return the release id to the client
        try:
            data = json.dumps({"release_id": new_user_release.id})
        except AttributeError:
            data = json.dumps({"release_id":new_user_release[0].id})

        return HttpResponse(data, content_type='application/json')
