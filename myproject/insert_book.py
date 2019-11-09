import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
import django
django.setup()
from openbooks.models import *

if __name__=='__main__':
    book =Book(title="파이썬 웹 프로그래밍", author=Author.objects.get(first_name="유", last_name="인근"), isbn="123-가나다", language=Language.objects.get(name="한국어"))
    book.save()
    # book.genre.add(Genre.objects.get(name="자기계발"))

    book =Book(title="Vue.js 마스터하기", author=Author.objects.get(first_name="이", last_name="두희"), isbn="456-라마바", language=Language.objects.get(name="중국어"))
    book.save()

    book =Book(title="떠나고싶다", author=Author.objects.get(first_name="", last_name="지숙"), isbn="789-아자차", language=Language.objects.get(name="한국어"))
    book.save()

    book =Book(title="맛있는 밥 하기", author=Author.objects.get(first_name="오", last_name="승엽"), isbn="555-라라라", language=Language.objects.get(name="영어"))
    book.save()

    book =Book(title="벌써 10시네", author=Author.objects.get(first_name="권", last_name="택준"), isbn="888-마마마", language=Language.objects.get(name="스페인어"))
    book.save()