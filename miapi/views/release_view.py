from django.http import HttpResponse
from miapi.models import Release
from rest_framework import viewsets
import json

class ReleaseView(viewsets.ViewSet):
    '''
    API endpoint that allows releases to be added to the database.
    '''

    def add_release(self, request):
        '''
        Handles the creation of a new release.

        Arguments:
        request -- The full HTTP request object.

        Returns:
        An Http repsonese that contains the release id.
        '''

        # Load the JSON string of the request body into a dict
        req_body = json.loads(request.body.decode())

        # Pass the request elements to the new release
        new_release = Release.objects.get_or_create(
            title=req_body['title'],
            catalog_number=req_body['catalog_number'],
            image=req_body['image'],
            year=req_body['year'],
            release_type_id=req_body['release_type'],
            label=req_body['label']
            )

        # Return the new release id to the client
        try:
            data = json.dumps({"release_id": new_release.id})
        except AttributeError:
            data = json.dumps({"release_id":new_release[0].id})

        return HttpResponse(data, content_type='application/json')


