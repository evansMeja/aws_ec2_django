from django.shortcuts import render
from django.http import *

def index(request):
    return HttpResponse("<h1>This is amazing cosing...</h1>")
