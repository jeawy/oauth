from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from apps import AppViews 

urlpatterns = [
    url(r'^products/$', AppViews.as_view(), name='products'),   
    url(r'^products/(?P<pk>[0-9]+)/$', AppViews.as_view(), name='detail'),  
    url(r'^products/(?P<pk>[0-9]+)/change$', AppViews.change , name='change'),   
]
