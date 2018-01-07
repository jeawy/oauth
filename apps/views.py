# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views import View
from django.utils.translation import ugettext as _
from django.http import HttpResponse,HttpResponseRedirect
from django.conf import settings
from django.shortcuts import redirect 
from django.http import Http404, QueryDict
import pdb
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import  Group
import os
from appuser.models import AdaptorUser as User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

import json
import random
import string
from django.utils import timezone
from django.core.urlresolvers import reverse
from apps.models import Apps

from django.contrib import auth

from basedatas.bd_comm import Common
from mobile.detectmobilebrowsermiddleware import DetectMobileBrowser

dmb     = DetectMobileBrowser()
comm    = Common()

 
class AppViews(View):

    @method_decorator(login_required)
    @method_decorator(permission_required('apps.manage_apps' , raise_exception=True))
    def get(self, request):
        isMble  = dmb.process_request(request)
        content = {} 
        apps = Apps.objects.all() 
        
        content['apps'] = apps  
         
        if 'new' in request.GET:
            if isMble:
                return render(request, 'apps/apps.html', content)
            else:
                return render(request, 'apps/apps.html', content) 
        else:
            if isMble:
                return render(request, 'apps/apps.html', content)
            else:
                return render(request, 'apps/apps.html', content)
 
    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def post(self, request):
        """
        新建
            删除：参数中带有method，并且值是'delete'，大小写不敏感
                # # id【必须字段】：Apps id 
            修改：参数中带有method，并且值是'put'，大小写不敏感
                # id【必须字段】：Apps id 
                # appname【可选字段】：Apps 名称 
          
            新建: 参数中带没有method，或method的值不等于put或者delete
                # appname【必须字段】：Apps 名称  
        """ 
        
        if 'method' in request.POST:
            method = request.POST['method'].lower()
            if method == 'put':# 修改
                return self.put(request)
            elif method == 'delete': # 删除
                return self.delete(request) 
            elif method == 'create': # 创建
                return self.create(request) 
        else:
            return self.create(request)
        
    
    def create(self, request):
        """创建"""
        # 新建Apps 
        # appname字段是必须的,uuid和secret是自动生成的
        user = request.user
        result = {}
        if 'appname' in request.POST : 
            appname = request.POST['appname'].strip() 
            # 创建Apps  
            newapp = Apps.objects.create_app(appname = appname) 
            result['status'] ='ok'
            result['msg'] = _('Created sucessfully') 
        else:
            result['status'] ='error'
            result['msg'] =_('Need appname in POST')
        return self.httpjson(result)

    def put(self, request):
        """
        修改 app名称
        """
        result = {}  
        data = QueryDict(request.body.decode('utf-8'))  
        if 'id' in data:
            appid = data['id']
            try:
                app = Apps.objects.get(id=appid)
                if 'appname' in data:
                    appname = data['appname']
                    app.appname = appname
                  
                app.save() 
                result['status'] ='ok'
                result['msg'] = _('Modified sucessfully')
            except Apps.DoesNotExist:
                result['status'] ='error'
                result['msg'] ='404 Not found the Product ID:{}'.format(appid) 
        else:
            result['status'] ='error'
            result['msg'] ='Need id  in POST'


        return self.httpjson(result)

    def delete(self, request):
        """
        删除指定Apps 
        """
        result = {} 
        data = QueryDict(request.body.decode('utf-8')) 
        if 'id' in data:
            appid = data['id'] 
            try: 
                app = Apps.objects.get(id=appid)
                app.delete() 
                result['status'] ='ok'
                result['msg'] = _('Done sucessfully')
            except Apps.DoesNotExist:
                result['status'] ='error'
                result['msg'] ='404 Not found the id {}'.format(appid) 
        else:
            result['status'] ='error'
            result['msg'] ='Need id in POST'

        return self.httpjson(result)
 
    def httpjson(self, result): 
        return HttpResponse(json.dumps(result), content_type="application/json")
