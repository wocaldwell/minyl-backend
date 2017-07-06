from django.http import HttpResponse
from miapi.models import UserRelease
from rest_framework import viewsets
import json



class DeleteUserReleaseView(viewsets.ViewSet):
    '''
    API endpoint that allows artists to be added to the database.
    '''

    def delete_user_release(self, request):
        '''
        Handles the deletion of user release relationship.

        Method arguments:
        request -- The full HTTP request object.

        Returns:
        An Http response wwith an 'okay' status.
        '''

        # Load the JSON string of the request body into a dict
        release_id_request = json.loads(request.body.decode())


        user_release = UserRelease.objects.get(user=request.user, release_id=release_id_request['release_id']).delete()


        return HttpResponse('user release removed', status=200)