import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_nexus.settings')
try:
    django.setup()
    print(f"DB User: {settings.DATABASES['default']['USER']}")
    print(f"DB Password: '{settings.DATABASES['default']['PASSWORD']}'")
except Exception as e:
    print(f"Setup failed: {e}")
