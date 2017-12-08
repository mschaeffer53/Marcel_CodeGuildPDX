from django.conf.urls import url, include

from . import views


app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^createUser/$', views.createUser, name='createUser'),
    url(r'^registration/$', views.registration_page, name='registration_page'),
    url(r'^blogPosts/$', views.blogPosts, name='blogPosts'),
    url(r'^blogFeed/$', views.blogFeed, name='blogFeed'),
    url(r'^createposts/$', views.create_post, name='create_post'),
    url(r'^mylogin/$', views.mylogin, name='mylogin'),
    url(r'^logout_view/$', views.logout_view, name='logout_view'),
    url(r'^(?P<pk>[0-9]+)/$', views.singlepost, name='singlepost')
]
