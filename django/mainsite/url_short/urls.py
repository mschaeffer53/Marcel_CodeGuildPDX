from django.conf.urls import url

from . import views


app_name = 'url_short'
urlpatterns = [
    url(r'^$', views.create_url, name='index'),
    url(r'^(?P<short>\w+)$', views.retrieve_url, name='redirect')
]
