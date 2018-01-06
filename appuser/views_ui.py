# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.conf import settings
from django.shortcuts import redirect 
import pdb
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import  Group
import os
from appuser.models import AdaptorUser as User
from appuser.models import VerifyCode
import json
import random
import string
from django.utils import timezone
from django.core.urlresolvers import reverse
 
from .form import UploadPortrainForm, GroupForm, UserForm

from django.contrib import auth

#from socialoauth import SocialSites,SocialAPIError  

from basedatas.bd_comm import Common
from mobile.detectmobilebrowsermiddleware import DetectMobileBrowser

dmb     = DetectMobileBrowser()
comm    = Common()

@csrf_exempt
def login(request):
    isMble  = dmb.process_request(request)
    
    if 'phone' in request.POST and 'password' in request.POST:
            auth.logout(request)
            phone       = request.POST['phone']
            password      = request.POST['password']
            user = auth.authenticate(phone=phone, password=password)
            if 'next' in request.GET: 
                next_url = request.GET.get('next')
            else:
                next_url = request.POST.get('next')
            context ={} 
            if user:
                # User is valid.  Set request.user and persist user in the session
                # by logging the user in.
                request.user = user
                auth.login(request, user)
                pdb.set_trace()
                # redirect to the value of next if it is entered, otherwise
                # to settings.APP_WEB_PC_LOGIN_URL
                next_url
                if next_url:
                    #after login, return to the previous page, but if the previous page is logout, 
                    #then return to the host page
                    if 'logout' not in str(next_url):
                         return redirect(next_url)
            
                return redirect('/')
            else:
                try: 
                    user_instance = User.objects.get(phone = phone)
                    msg = '登录失败，密码错误...' 
                except User.DoesNotExist:
                    msg = '登录失败，用户{0}未注册...'.format(phone)
                status = 'error' 
                context = {'next':next_url,
                           'status':'error',
                           'msg':msg,
                           'phone':phone}
            if isMble: 
                return render(request, 'user/m_login.html', context)
            else:
                return render(request, 'user/login.html', context)
            
    else:
        next_url = request.GET.get('next')
        context = {'next':next_url}

        if isMble: 
            return render(request, 'user/m_login.html', context)
        else:  
            return render(request, 'user/login.html', context)
def logout(request):
    auth.logout(request)
    return redirect('/')
   
@csrf_exempt
def register(request):
    content = {}

    if request.method == "POST":
        username = request.POST['username'].strip()
        phone = request.POST['phone'].strip()
        password = request.POST['password'].strip()
        phonecode = request.POST['phonecode'].strip()
        if VerifyCode.objects.veirfy_code_phone(phonecode, phone):
            user = User.objects.create_user(phone, username,  password)
     
            user = auth.authenticate(phone=phone, password=password)
            auth.login(request, user)
            content={
                'result':'ok',
                'msg':'注册成功！'
            }
             
        else:
            content={
                'result':'error',
                'username':username,
                'phone':phone, 
                'msg':'验证码错误...'
            }

        return render(request, 'user/regsiter.html', content)
    else: 
        return render(request, 'user/regsiter.html', content)

@csrf_exempt
def find_password(request):
    isMble  = dmb.process_request(request) 
    content={}
    if request.method == 'POST':
        phone = request.POST['phone'].strip()
        password = request.POST['password'].strip()
        phonecode = request.POST['phonecode'].strip()
        if VerifyCode.objects.veirfy_code_phone(phonecode, phone):
            user = User.objects.get(phone = phone )
            user.set_password(password) 
            user.save()

            user = auth.authenticate(phone=phone, password=password)
            auth.login(request, user)
            content={
                'result':'ok',
                'msg':'修改成功！',
                'pagetype':'findpassword',
            }
        else:
            content={
                'result':'error', 
                'phone':phone, 
                'pagetype':'findpassword',
                'msg':'验证码错误...'
            }
    else:
        content = {
            'page':'find_password',
            'pagetype':'findpassword',
            'page_title':'找回密码'
        }
    if isMble:
        return render(request, 'user/regsiter.html', content)
    else:
        return render(request, 'user/regsiter.html', content)