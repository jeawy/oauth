#! -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Apps(models.Model):
    """
    客户端信息表
    """
    secret = models.CharField(max_length = 128, null=True )
    uuid = models.CharField(max_length = 128, unique=True )
    appname = models.CharField(max_length = 128  )
    
    class Meta:
        pass
        
    def __str__(self):
        return self.appname


class AuthToken(models.Model):
    """

    """
    pass
