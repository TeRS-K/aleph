from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
# from db import login as db_login

# login function
def login(request):
    template = loader.get_template('profile/login.html')
    # function..
    return HttpResponse(template.render())

@csrf_exempt
def verify(request):
    params=""
    for key in request.POST:
        params += request.POST[key] + "\n"

    print(request.POST)
    return HttpResponse(params)


def register(request):
    template = loader.get_template('profile/register.html')
    return HttpResponse(template.render())

# logout function
def logout(request):
    template = loader.get_template('profile/login.html')
    # function..
    return HttpResponse(template.render())

def index(request):
    # Get an HttpRequest - the request parameter
    # perform operations using information from the request.
    # Return HttpResponse
    return HttpResponse('Hello from Django!')



# def update(request, ):



