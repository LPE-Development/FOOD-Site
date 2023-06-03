from django.http import HttpResponse
from django.shortcuts import render

from .models import *

menu = ['Home', 'Recipes', 'Traditional dishes', ' Healthy diet', 'Set in']

def index(request):
    posts = Recipes.objects.all()
    return render(request, 'foodbar/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})

def categories(request):
    return HttpResponse("22")