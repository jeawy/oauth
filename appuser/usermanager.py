from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser,PermissionsMixin
)
import pdb
 

class UserManager(BaseUserManager):
    def create_user(self, phone, name, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not phone:
            raise ValueError('Users must have an phone')

        user = self.model(
            phone=phone,
            username = name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone,  password, name):
        """
        Creates and saves a superuser with the given phone, date of
        birth and password.
        """
        user = self.create_user(phone,
            password=password,
            username = name
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    
    def uniqueUsername(self, username):
        """
        check if the username is unique
        if unique, return True
        else return False
        """
        try: 
            self.get(username=username)
            return False
        except self.model.DoesNotExist:
            return True
        except self.model.MultipleObjectsReturned:
            return False
    
    def uniqueEmail(self, email):
        """
        check if the email is unique
        if unique, return True
        else return False
        """
        try: 
            self.get(email=email)
            return False
        except self.model.DoesNotExist:
            return True
        except self.model.MultipleObjectsReturned:
            return False

class AdaptorUserManager(UserManager):
    def getsuperuser_emails(self ):
        """
        get super users email list
        """
        users = self.filter(is_superuser = 1)
        return [user.email for user in users]