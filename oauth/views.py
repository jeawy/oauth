from django.shortcuts import render 
from django.conf import settings
from django.utils.translation import activate
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
import pdb

def home(request):
    content ={}   
    content['mediaroot'] = settings.MEDIA_URL
    return render(request, 'home.html',content) 

def switch_language(request):
    content ={}   
    if 'django_language' in request.session: 
        if settings.LANGUAGE_CODE == 'en':
            activate('zh-hans')
            request.session['django_language'] = 'zh-hans'
            settings.LANGUAGE_CODE = 'zh-hans'
        else:
            activate('en')
            request.session['django_language'] = 'en'
            settings.LANGUAGE_CODE = 'en'
    else:
        activate('en')
        request.session['django_language'] = 'en'
        settings.LANGUAGE_CODE = 'en'

    return redirect('home') 