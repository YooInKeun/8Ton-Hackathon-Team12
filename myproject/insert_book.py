import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
import django
django.setup()
from openbooks.models import *

if __name__=='__main__':
    book =Book(title="당신은 왜 살아있는가?", author=Author.objects.get(first_name="지", last_name="상현"), isbn="321-두루미", language=Language.objects.get(name="한국어"))
    book.save()
    # book.genre.add(Genre.objects.get(name="자기계발"))

    book =Book(title="사랑합니다. 그대를", author=Author.objects.get(first_name="권", last_name="요한"), isbn="746-강한나", language=Language.objects.get(name="중국어"))
    book.save()

    book =Book(title="떠나고싶다2", author=Author.objects.get(first_name="권", last_name="소율"), isbn="789-차차차", language=Language.objects.get(name="한국어"))
    book.save()

    book =Book(title="밥만으론 살수없다", author=Author.objects.get(first_name="이", last_name="율"), isbn="424-추장사", language=Language.objects.get(name="영어"))
    book.save()

    book =Book(title="벌써 12시네", author=Author.objects.get(first_name="박", last_name="남준"), isbn="392-군사자", language=Language.objects.get(name="스페인어"))
    book.save()
    
    book =Book(title="당신은 왜 죽었다 생각하는가?", author=Author.objects.get(first_name="지", last_name="상현"), isbn="321-마루미", language=Language.objects.get(name="한국어"))
    book.save()
    # book.genre.add(Genre.objects.get(name="자기계발"))

    book =Book(title="싫어합니다. 그대를", author=Author.objects.get(first_name="권", last_name="요한"), isbn="746-나한나", language=Language.objects.get(name="중국어"))
    book.save()

    book =Book(title="여기있자", author=Author.objects.get(first_name="권", last_name="소율"), isbn="789-차차타", language=Language.objects.get(name="한국어"))
    book.save()

    book =Book(title="당신없인 살수없다", author=Author.objects.get(first_name="이", last_name="율"), isbn="411-추장사", language=Language.objects.get(name="영어"))
    book.save()

    book =Book(title="벌써?", author=Author.objects.get(first_name="박", last_name="남준"), isbn="392-군사타", language=Language.objects.get(name="스페인어"))
    book.save()