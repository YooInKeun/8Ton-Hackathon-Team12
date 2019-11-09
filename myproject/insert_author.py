import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
import django
django.setup()
from openbooks.models import *

if __name__=='__main__':
    Author(first_name="유", last_name="인근", date_of_birth="2019-11-09", date_of_death="2019-11-10").save()
    Author(first_name="오", last_name="승엽", date_of_birth="2019-11-09", date_of_death="2019-11-10").save()
    Author(first_name="권", last_name="택준", date_of_birth="2019-11-09", date_of_death="2019-11-10").save()
    Author(first_name="이", last_name="두희", date_of_birth="2019-11-09", date_of_death="2019-11-10").save()
    Author(first_name="", last_name="지숙", date_of_birth="2019-11-09", date_of_death="2019-11-10").save()