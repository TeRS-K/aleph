from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .db import login as db_login
from .db import registration as db_registration

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

    username = "'{}'".format(request.POST['username'])
    password = "{}".format(request.POST['password'])

    print(username, password)
    template = ""

    if (db_login.login(username, password) == -1):
        messages.info(request, "Failed")
        template = loader.get_template('profile/login.html')
    else:
        messages.info(request, "OK")
        template = loader.get_template('profile/index.html')
    
    return HttpResponse(template.render())

def register(request):
    template = loader.get_template('profile/register.html')
    return HttpResponse(template.render())

@csrf_exempt
def new_user(request):
    params=""
    for key in request.POST:
        params += request.POST[key] + "\n"

    username = "{}".format(request.POST['username'])
    password = request.POST['password']
    print(username, password)
    template = ""

    if (db_registration.new_user(username, password) == 1):
        messages.info(request, "OK")
        template = loader.get_template('profile/login.html')
    else:
        messages.info(request, "Shit")
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



