import uuid
from django.db import models
 
import pdb
 

class AppManager(models.Manager):
    """
    apps manager
    """

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
 
   
class AuthTokenManager(models.Manager):
    """
    auth token manager
    """

    def create_token(self, app, user ):
        """
        Creates app and generate uuid and secret.
        """ 
        authtoken, created = self.get_or_create( app = app, user = user) 
        authtoken.token = uuid.uuid4() 
        authtoken.save(using=self._db)
        return authtoken.token