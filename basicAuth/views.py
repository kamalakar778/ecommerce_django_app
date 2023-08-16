from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def register(request):
    return render(request, "/Sign-In")

def signin(request):
    return HttpResponse("Sign In Page") #render(request, "signin.html")

def signout(request):
    return HttpResponse("Sign Out Page") #render(request, "signout.html")