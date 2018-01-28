from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader


# login function
def login(request):
    template = loader.get_template('profile/login.html')
    return HttpResponse(template.render())

def register(request):
    template = loader.get_template('profile/register.html')
    return HttpResponse(template.render())


# logout function
def logout(request):
    template = loader.get_template('profile/login.html')
    # function..
    return HttpResponse(template.render())

# def update(request, ):



