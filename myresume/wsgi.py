# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myresume.settings')

# application = get_wsgi_application()



import os
import sys

# Add your project directory to the sys.path
project_home = '/home/otisamueloti/myresume'
if project_home not in sys.path:
    sys.path.append(project_home)

# Set environment variables
os.environ['DJANGO_SETTINGS_MODULE'] = 'myresume.settings'
os.environ['PYTHON_EGG_CACHE'] = '/tmp'

# Activate virtualenv
activate_this = os.path.join(project_home, 'venv/bin/activate_this.py')
exec(open(activate_this).read(), {'__file__': activate_this})

# Initialize Django application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

