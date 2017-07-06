from django.http import HttpResponse
from miapi.models import UserRelease
import json
from rest_framework import viewsets



class UpdateUserReleaseView(viewsets.ViewSet):
    '''
    API endpiont that handles the changing of a release from want to own.
    '''

    def update_user_release(self, request):
        '''
        Handles the creation of a new user release relationship.

        Arguments:
        request -- The full HTTP request object.

        Returns:
        An Http response that includes the updated release.
        '''

        # Load the JSON string of the request body into a dict
        release_id_request = json.loads(request.body.decode())

        # Filter a release by the request release id and change the own status
        updated_user_release = UserRelease.objects.filter(user=request.user, release_id=release_id_request['release_id']).update(own=1)

        # Return the release id to the client
        data = json.dumps({"release": updated_user_release})
        return HttpResponse(data, content_type='application/json')