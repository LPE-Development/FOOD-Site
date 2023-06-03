from django.http import HttpResponse
from django.shortcuts import render




def index(request):
    return HttpResponse("11")

def categories(request):
    return HttpResponse("22")