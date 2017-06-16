from django.http import HttpResponse
from miapi.models import UserRelease
import json
from rest_framework import viewsets



class AddUserReleaseView(viewsets.ViewSet):

    def add_user_release(self, request):
        '''Handles the creation of a new user release relationship

        Method arguments:
          request -- The full HTTP request object
        '''

        # Load the JSON string of the request body into a dict
        req_body = json.loads(request.body.decode())

        new_user_release = UserRelease(
            user=request.user,
            release_id=req_body['release_id'],
            own=req_body['own'],
            )

        # Commit the release to the database by saving it
        new_user_release.save()

        return HttpResponse('user release added to db!!!!!!!!!!!!!!!!!')
