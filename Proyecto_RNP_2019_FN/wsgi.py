"""
WSGI config for Proyecto_RNP_2019_FN project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Proyecto_RNP_2019_FN.settings')
#from whitenoise.django import DjangoWhiteNoise

application = get_wsgi_application()

#application = DjangoWhiteNoise(application)