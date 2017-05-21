"""
WSGI config for lendit project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

sys.path.append('/home/lendituser/lendit')
sys.path.append('/home/lendituser/lendit/lendit')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lendit.settings")

application = get_wsgi_application()
