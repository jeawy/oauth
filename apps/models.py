#! -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from apps.appmanager import AppManager, AuthTokenManager
from appuser.models import AdaptorUser as User
class Apps(models.Model):
    """
    客户端信息表
    """
    secret = models.CharField(max_length = 128, null=True )
    uuid = models.CharField(max_length = 128, unique=True )
    appname = models.CharField(max_length = 128  )
    objects = AppManager()
    
    class Meta:
        permissions=(
            ('manage_apps', _('manage apps:create, delete')),
        )
        
    def __str__(self):
        return self.appname


class AuthToken(models.Model):
    """
    授权表
    """
    user = models.ForeignKey(User)
    app = models.ForeignKey(Apps)
    token = models.CharField(max_length = 128, unique = True)
    objects = AuthTokenManager()

    class Meta:
        unique_together=(("user", "app"),)
        
