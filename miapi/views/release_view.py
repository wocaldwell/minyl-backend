from django.http import HttpResponse
from miapi.models import Release
from django.views.decorators.csrf import csrf_exempt

import json

@csrf_exempt
def add_release(request):
    '''
    Handles the creation of a new release

    Method arguments:
      request -- The full HTTP request object
    '''

    # Load the JSON string of the request body into a dict
    req_body = json.loads(request.body.decode())

    new_release = Release.objects.get_or_create(
        title=req_body['title'],
        catalog_number=req_body['catalog_number'],
        image=req_body['image'],
        year=req_body['year'],
        release_type_id=req_body['release_type'],
        )

    # Return the new release id to the client
    try:
        data = json.dumps({"release_id": new_release.id})
    except AttributeError:
        data = json.dumps({"release_id":new_release[0].id})

    return HttpResponse(data, content_type='application/json')
