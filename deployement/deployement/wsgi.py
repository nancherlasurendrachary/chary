import os

import sys


path = '/home/rajwilsonn/deployement/deployement/'

if path not in sys.path:

    sys.path.append(path)



from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'deployement.settings')


application = get_wsgi_application()
