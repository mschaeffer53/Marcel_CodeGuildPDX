from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Url
# Create your views here.

import random

def rand_string():
    chars = 'qawsedrftgyhujikolpzsxdcfvgbhnjmk1234567890'
    rand_short = ''
    while len(rand_short)<10:
        char = random.choice(chars)
        rand_short += char
    return rand_short


def temp(request):
    return HttpResponse('temp')

def create_url(request):
    short = ''
    if request.method == 'POST':
        short = rand_string()
        new_url = Url(url=request.POST['url'], short=short)
        new_url.save()
    return render(request, 'url_short/create.html', {'short_url': short})

def retrieve_url(request, short):
    short_url = get_object_or_404(Url, short=short)
    x = short_url.url
    return HttpResponseRedirect('http://' + x)
