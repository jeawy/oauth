from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from apps.views import AppViews 

urlpatterns = [
    url(r'^apps/$', AppViews.as_view(), name='apps'),   
    url(r'^apps/(?P<pk>[0-9]+)/$', AppViews.as_view(), name='detail'),  
    #url(r'^apps/(?P<pk>[0-9]+)/change$', AppViews.change , name='change'),   
]
