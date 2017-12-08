from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Blogpost, Comment
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def index(request):
    return render(request, 'blog/index.html', {})

def createUser(request):
    group = Group.objects.get(name='Commenters')
    print(request.POST)
    name = request.POST['user_name']
    password = request.POST['password']
    # Create user and save to the database
    user = User.objects.create_user(name, 'fake@email.com', password)
    user.save()
    group.user_set.add(user)
    group.save()
    return HttpResponseRedirect(reverse('blog:blogFeed'))


def registration_page(request):
    return render(request, 'blog/createUser.html', {})

def blogPosts(request):
    # @login_required
    return render(request, 'blog/blogPosts.html', {})

def create_post(request):


    body = request.POST['body']
    title = request.POST['title']


    blog = Blogpost(title=title, body=body, user=request.user)
    blog.save()


    return HttpResponseRedirect(reverse('blog:blogFeed'))

def blogFeed(request):
    posts = Blogpost.objects.all()
    return render(request, 'blog/blogFeed.html', {'blog': posts})

def mylogin(request):
    # retrieve the variables from the form submission
    username = request.POST['user_name']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('blog:blogFeed'))
    else:
        return HttpResponse('invalid credentials')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('blog:index'))

def singlepost(request, pk):
    post = get_object_or_404(Blogpost, pk=pk)

    return render(request, 'blog/singlepost.html', {'post': post})