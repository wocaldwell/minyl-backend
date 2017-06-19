from django.http import HttpResponse
from miapi.models import UserRelease
import json
from rest_framework import viewsets



class UpdateUserReleaseView(viewsets.ViewSet):

    def update_user_release(self, request):
        '''Handles the creation of a new user release relationship

        Method arguments:
          request -- The full HTTP request object
        '''

        # Load the JSON string of the request body into a dict
        release_id_request = json.loads(request.body.decode())
        print(release_id_request, '-----------------')

        updated_user_release = UserRelease.objects.filter(pk=release_id_request['release_id']).update(own=1)

        # Return the release id to the client
        data = json.dumps({"release": updated_user_release})


        return HttpResponse(data, content_type='application/json')