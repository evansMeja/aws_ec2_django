from django.shortcuts import render
from django.http import *

def index(request):
    template_name="public/index.html"
    context={}
    return render(request,template_name,context)
