from django.http import HttpResponse
from miapi.models import UserRelease
import json
from rest_framework import viewsets



class DeleteUserReleaseView(viewsets.ViewSet):

    def delete_user_release(self, request):
        '''Handles the deletion of user release relationship

        Method arguments:
          request -- The full HTTP request object
        '''

        # Load the JSON string of the request body into a dict
        release_id_request = json.loads(request.body.decode())


        user_release = UserRelease.objects.get(user=request.user, release_id=release_id_request['release_id']).delete()


        return HttpResponse('relationship absolved')