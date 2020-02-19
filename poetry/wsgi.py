"""
WSGI config for poetry project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
###############################
from whitenoise import WhiteNoise

from my_project import MyWSGIApp

application = MyWSGIApp()
application = WhiteNoise(application, root=os.path.join(BASE_DIR, 'staticfiles'))
###############################

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'poetry.settings')