from django.conf.urls import url

from . import views


app_name = 'library'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^checkout/$', views.checkout, name='checkout'),
    url(r'^checkin/$', views.checkin, name='checkin'),
    url(r'^rentallog/$', views.rentallog, name='rentallog')
]
