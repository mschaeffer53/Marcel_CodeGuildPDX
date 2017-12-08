from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

#from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout

# from .models import NEWMODEL

# Create your views here.

def index(request):
    return render(request, 'doggonnit/index.html', {})