from django.shortcuts import render 
from django.conf import settings
from django.utils.translation import activate
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
import pdb
from apps.models import AuthToken, Apps
from appuser.models import AdaptorUser as User
from django.contrib.auth.decorators import login_required

@login_required
def home(request, *args , **kwargs):
    content ={}   
     
    content['mediaroot'] = settings.MEDIA_URL 
    user = request.user
    apps = Apps.objects.all()
    appid = []
    for app in apps:
        appid.append(app.id)
    #User.objects.all().delete() 

    if not user.is_anonymous():
        tokens = AuthToken.objects.filter(user = user, app__id__in = appid)
        content['tokens'] = tokens

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