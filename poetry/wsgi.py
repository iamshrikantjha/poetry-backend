import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'poetry.settings')

###############################
from whitenoise import WhiteNoise


from poetry.wsgi import poetry

application = PoetryApplication(application)
application = WhiteNoise(application, root=os.path.join(BASE_DIR, 'staticfiles'))
###############################

