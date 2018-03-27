#! -*- coding:utf-8 -*- 
from django.db import models
import pdb
import random
import string
from django.conf import settings
from common.e_mail import EmailEx
import requests

class CodeManager(models.Manager):
    """
    验证码的manager
    """
    email = EmailEx()
     
    def generate_code(self):
        code    = ''.join(random.choice(string.digits) for i in range(4))
        return code

    def send_code(self, email):
        result={} 
        if not self.email.EMAIL_REGEX.match(email):
            result['status'] = 1
            result['msg'] = '电子邮件格式不正确'
        else: 
            code    =  self.generate_code()
            Subject = settings.PROJECTNAME+'邮箱验证' 
            content = '您好， 欢迎您注册'+settings.PROJECTNAME+'，您的邮箱验证码是： ' + code
            try:
                self.email.send_text_email(Subject, content, email) 
                try:
                    verify_code = self.model.objects.get(email__exact = email, type ='0')
                    verify_code.code = code
                    verify_code.save()
                except self.model.DoesNotExist:
                    verify_code = self.model(email=email, code=code, type ='0')
                    verify_code.save()
                    
                result['status'] = 2
                result['msg'] = '验证码已发至您的邮箱中， 请到邮箱中查看您的验证码!'  
            except Exception as e:
                result['status'] = 3 
                result['msg'] = '发送邮件的过程中发生错误： '+ str(e)

        return result
    
    def veirfy_code(self, code, email): 
        try:
            verify_code = self.model.objects.get(email__exact = email, code =code)
            return True
        except self.model.DoesNotExist:
            return False

class PhoneCodeManager(CodeManager):
    """
    验证码的manager
    """
     
      
    def send_code_phone(self, phone, codetype):
        result={}  
        code    = self.generate_code()
        Subject = settings.PROJECTNAME + '手机验证' 
        content = "【"+settings.PROJECTNAME+"】 您好， 您的手机验证码是:"+ code + " 请勿转发给他人。"
        print (code)
        
        req = requests.get(settings.SMS_API.format(phone,content)) 
        try:
            # send phone code from a SDK 
            try:
                verify_code = self.model.objects.get(phone__exact = phone, type =codetype)
                verify_code.code = code
                verify_code.save()
            except self.model.DoesNotExist:
                verify_code = self.model(phone=phone, code=code, type = codetype)
                verify_code.save()
                
            result['status'] = 'ok'
            result['msg'] = '验证码已发至您的手机中.'  
        except Exception as e:
            result['status'] = 'error' 
            result['msg'] = '发送手机验证码的过程中发生错误： '+ str(e)

        return result
    
    def veirfy_code_phone(self, code, phone): 
        """
        获取手机验证码
        """
        try:
            verify_code = self.model.objects.get(phone__exact = phone, code =code)
            return True
        except self.model.DoesNotExist:
            return False
class AdaptorCodeManager(PhoneCodeManager):
    pass