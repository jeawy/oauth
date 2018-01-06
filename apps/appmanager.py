import uuid
from django.db import models
 
import pdb
 

class AppManager(models.Manager):
    def create_app(self, appname ):
        """
        Creates app and generate uuid and secret.
        """
        if not appname:
            raise ValueError('appname can not be empty.')

        app = self.model( appname=appname ) 
        app.uuid = uuid.uuid4()
        app.secret = uuid.uuid4()
        app.save(using=self._db)
        return app
 
   
class AdaptorUserManager(AppManager):
    pass