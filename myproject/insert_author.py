import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
import django
django.setup()
from openbooks.models import *

if __name__=='__main__':
    Author(first_name="이", last_name="기광", date_of_birth="1984-12-17").save()
    Author(first_name="지", last_name="상현", date_of_birth="1993-06-19", date_of_death="2018-10-10").save()
    Author(first_name="권", last_name="요한", date_of_birth="1964-04-14", date_of_death="2010-01-10").save()
    Author(first_name="박", last_name="남준", date_of_birth="1997-01-23", date_of_death="2010-11-10").save()
    Author(first_name="남궁", last_name="한수", date_of_birth="2000-12-29", date_of_death="2014-11-10").save()
    Author(first_name="남", last_name="수자", date_of_birth="1976-09-01").save()
    Author(first_name="오", last_name="충환", date_of_birth="1977-08-03").save()
    Author(first_name="정", last_name="덕만", date_of_birth="1976-10-06").save()
    Author(first_name="장", last_name="광만", date_of_birth="1997-10-28").save()
    Author(first_name="강", last_name="박민", date_of_birth="1999-05-16").save()
    Author(first_name="권", last_name="소율", date_of_birth="1978-04-17").save()
    Author(first_name="남", last_name="예슬", date_of_birth="1965-03-24").save()
    Author(first_name="이", last_name="율", date_of_birth="1990-01-10").save()
    Author(first_name="김", last_name="나레", date_of_birth="1996-02-20").save()
    Author(first_name="김", last_name="지혜", date_of_birth="2001-06-22").save()