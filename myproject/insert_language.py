import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
import django
django.setup()
from openbooks.models import *

if __name__=='__main__':
    Language(name="한국어").save()
    Language(name="영어").save()
    Language(name="중국어").save()
    Language(name="스페인어").save()
    Language(name="포트투갈어").save()