import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
import django
django.setup()
from openbooks.models import *

if __name__=='__main__':
    BookInstance(book=Book.objects.get(title__startswith="사랑합니다."), summary="별로 읽지 않은 책이라, 양호합니다!", rent_availability=True, donate_availability=False, location_longitude=129.48590, location_latitude=33.584862).save()
    BookInstance(book=Book.objects.get(title__startswith="밥만으론 살수"), summary="Vue.js 책 기부합니다! 깔끔하게 사용했습니다", rent_availability=False, donate_availability=True, location_longitude=124.2485, location_latitude=37.084862).save()
    BookInstance(book=Book.objects.get(title__startswith="벌써 12"), summary="상태는 별로 안좋지만, 쓸만합니다!", rent_availability=False, donate_availability=True, location_longitude=126.22590, location_latitude=40.424862).save()
    BookInstance(book=Book.objects.get(title__startswith="싫어합니"), summary="상태는 괜찮습니다, 책 좋습니다!", rent_availability=True, donate_availability=False, location_longitude=122.48590, location_latitude=30.884862).save()
    BookInstance(book=Book.objects.get(title__startswith="사랑합니다."), summary="별로 읽지 않은 책이라, 양호합니다!", rent_availability=True, donate_availability=False, location_longitude=129.48590, location_latitude=33.584862).save()
    BookInstance(book=Book.objects.get(title__startswith="밥만으론 살수"), summary="Vue.js 책 기부합니다! 깔끔하게 사용했습니다", rent_availability=False, donate_availability=True, location_longitude=125.2485, location_latitude=36.084862).save()
    BookInstance(book=Book.objects.get(title__startswith="벌써 12"), summary="상태는 별로 안좋지만, 쓸만합니다!", rent_availability=False, donate_availability=True, location_longitude=125.22590, location_latitude=49.424862).save()
    BookInstance(book=Book.objects.get(title__startswith="싫어합니"), summary="상태는 괜찮습니다, 책 좋습니다!", rent_availability=True, donate_availability=False, location_longitude=121.48590, location_latitude=29.884862).save()
    BookInstance(book=Book.objects.get(title__startswith="사랑합니다."), summary="별로 읽지 않은 책이라, 양호합니다!", rent_availability=True, donate_availability=False, location_longitude=130.48590, location_latitude=34.584862).save()
    BookInstance(book=Book.objects.get(title__startswith="밥만으론 살수"), summary="Vue.js 책 기부합니다! 깔끔하게 사용했습니다", rent_availability=False, donate_availability=True, location_longitude=125.2485, location_latitude=38.084862).save()
    BookInstance(book=Book.objects.get(title__startswith="벌써 12"), summary="상태는 별로 안좋지만, 쓸만합니다!", rent_availability=False, donate_availability=True, location_longitude=127.22590, location_latitude=41.424862).save()
    BookInstance(book=Book.objects.get(title__startswith="싫어합니"), summary="상태는 괜찮습니다, 책 좋습니다!", rent_availability=True, donate_availability=False, location_longitude=120.48590, location_latitude=28.884862).save()
    BookInstance(book=Book.objects.get(title__startswith="사랑합니다."), summary="별로 읽지 않은 책이라, 양호합니다!", rent_availability=True, donate_availability=False, location_longitude=127.48590, location_latitude=31.584862).save()
    BookInstance(book=Book.objects.get(title__startswith="밥만으론 살수"), summary="Vue.js 책 기부합니다! 깔끔하게 사용했습니다", rent_availability=False, donate_availability=True, location_longitude=122.2485, location_latitude=35.084862).save()
    BookInstance(book=Book.objects.get(title__startswith="벌써 12"), summary="상태는 별로 안좋지만, 쓸만합니다!", rent_availability=False, donate_availability=True, location_longitude=123.22590, location_latitude=37.424862).save()
    BookInstance(book=Book.objects.get(title__startswith="싫어합니"), summary="상태는 괜찮습니다, 책 좋습니다!", rent_availability=True, donate_availability=False, location_longitude=119.48590, location_latitude=27.884862).save()
    BookInstance(book=Book.objects.get(title__startswith="사랑합니다."), summary="별로 읽지 않은 책이라, 양호합니다!", rent_availability=True, donate_availability=False, location_longitude=126.48590, location_latitude=30.584862).save()
    BookInstance(book=Book.objects.get(title__startswith="밥만으론 살수"), summary="Vue.js 책 기부합니다! 깔끔하게 사용했습니다", rent_availability=False, donate_availability=True, location_longitude=124.2485, location_latitude=37.084862).save()
    BookInstance(book=Book.objects.get(title__startswith="벌써 12"), summary="상태는 별로 안좋지만, 쓸만합니다!", rent_availability=False, donate_availability=True, location_longitude=126.22590, location_latitude=40.424862).save()
    BookInstance(book=Book.objects.get(title__startswith="싫어합니"), summary="상태는 괜찮습니다, 책 좋습니다!", rent_availability=True, donate_availability=False, location_longitude=122.48590, location_latitude=30.884862).save()
    BookInstance(book=Book.objects.get(title__startswith="사랑합니다."), summary="별로 읽지 않은 책이라, 양호합니다!", rent_availability=True, donate_availability=False, location_longitude=129.48590, location_latitude=33.584862).save()
    BookInstance(book=Book.objects.get(title__startswith="밥만으론 살수"), summary="Vue.js 책 기부합니다! 깔끔하게 사용했습니다", rent_availability=False, donate_availability=True, location_longitude=124.2485, location_latitude=37.084862).save()
    BookInstance(book=Book.objects.get(title__startswith="벌써 12"), summary="상태는 별로 안좋지만, 쓸만합니다!", rent_availability=False, donate_availability=True, location_longitude=126.22590, location_latitude=40.424862).save()
    BookInstance(book=Book.objects.get(title__startswith="싫어합니"), summary="상태는 괜찮습니다, 책 좋습니다!", rent_availability=True, donate_availability=False, location_longitude=122.48590, location_latitude=30.884862).save()