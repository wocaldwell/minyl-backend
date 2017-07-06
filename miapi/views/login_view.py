from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from miapi.models import *

@csrf_exempt
def login_user(request):
    '''
    Handles the creation of a new user for authentication.

    Arguments:
    request -- The full HTTP request object.

    Returns:
    An Http response that confirms the status of the supplied credentials.
    '''

    # Load the JSON string of the request body into a dict
    req_body = json.loads(request.body.decode())

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':

        # Use the built-in authenticate method to verify
        username=req_body['username']
        password=req_body['password']
        authenticated_user = authenticate(username=username, password=password)

        # If authentication was successful, log the user in
        if authenticated_user is not None:
            login(request=request, user=authenticated_user)

            return HttpResponse(status=200)

        else:
            # Bad login details were provided. So we can't log the user in.
            return HttpResponse("Invalid login details supplied.")
