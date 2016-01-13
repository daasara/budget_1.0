import os
import sys

path = '/home/alexey/sites/budget_1.0'
if path not in sys.path:
    sys.path.append(path)

lib_path = '/home/alexey/.virtualenvs/budget1/lib/python3.4/site-packages'
if lib_path not in sys.path:
    sys.path.append(lib_path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'budget.settings'

#import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler()
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
