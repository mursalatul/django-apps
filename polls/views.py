from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request, app_name):
    return HttpResponse("Hello, world. You're at the polls index.")