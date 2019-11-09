import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
import django
django.setup()
from openbooks.models import *

if __name__=='__main__':
    Genre(name="자기계발").save()
    Genre(name="인문, 심리, 철학").save()
    Genre(name="시, 에세이").save()
    Genre(name="경제, 경영").save()
    Genre(name="만화").save()
    Genre(name="여행").save()
    