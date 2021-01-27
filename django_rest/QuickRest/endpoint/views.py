from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homer(request):
    return HttpResponse("hi this is a view")
