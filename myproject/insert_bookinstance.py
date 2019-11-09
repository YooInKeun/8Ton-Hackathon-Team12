import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
import django
django.setup()
from openbooks.models import *

if __name__=='__main__':
    BookInstance(book=Book.objects.get(title="Vue.js 마스터하기"), summary="별로 읽지 않은 책이라, 양호합니다!", rent_availability=True, donate_availability=False, location_longitude=127.48590, location_latitude=38.584862).save()
    BookInstance(book=Book.objects.get(title="Vue.js 마스터하기"), summary="Vue.js 책 기부합니다! 깔끔하게 사용했습니다", rent_availability=False, donate_availability=True, location_longitude=127.2485, location_latitude=38.084862).save()
    BookInstance(book=Book.objects.get(title="맛있는 밥 하기"), summary="상태는 별로 안좋지만, 쓸만합니다!", rent_availability=False, donate_availability=True, location_longitude=127.22590, location_latitude=38.424862).save()
    BookInstance(book=Book.objects.get(title="Vue.js 마스터하기"), summary="상태는 괜찮습니다, 책 좋습니다!", rent_availability=True, donate_availability=False, location_longitude=127.48590, location_latitude=38.884862).save()