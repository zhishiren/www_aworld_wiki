"""
WSGI config for aworld2024 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""
import os
import sys


from django.core.wsgi import get_wsgi_application
print("Python executable: ", sys.executable)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aworld2024.settings')

application = get_wsgi_application()
