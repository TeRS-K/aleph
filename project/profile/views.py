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
        return render(request, "profile/login.html")
        # template = loader.get_template('profile/login.html')
    else:
        messages.info(request, "OK")
        return render(request, "profile/verify.html")
        # template = loader.get_template('profile/verify.html')
    
    return HttpResponse("LMAO")

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
    template = ""

    val = db_registration.new_user(username, password)
    print(val)
    if (val == 1):
        messages.info(request, "OK")
        # template = loader.get_template('profile/login.html')
        return render(request, 'profile/login.html')
    else:
        messages.info(request, "Fail")
        # template = loader.get_template('profile/register.html')
        return render(request, 'profile/register.html')

# logout function
def logout(request):
    template = loader.get_template('profile/login.html')
    # function..
    return HttpResponse(template.render())

def index(request):
    template = loader.get_template('/profile/static/profile/bootstrap/main.html')
    return HttpResponse(template.render())



# def update(request, ):



