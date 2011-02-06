import os, sys

sys.path.append('/var/www/html')
sys.path.append('/usr/lib/python2.6/site-packages/django/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'magicblog.settings_production'

 

import django.core.handlers.wsgi

 

application = django.core.handlers.wsgi.WSGIHandler()
