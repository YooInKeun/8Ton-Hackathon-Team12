from django.test import TestCase
from django.urls import reverse
from .models import BookInstance, Language, Book, Author, Genre

import datetime

# Create your tests here.
class ManyToManyCreationTestCase(TestCase):
    def setUp(self):
        Language.objects.create(name="한국어")
        Book.objects.create(title="트렌드 코리아 2020", isbn="9788959896127", language=Language.objects.get(name__icontains="한국"))
        Book.objects.create(title="천 번을 흔들려야 어른이 된다", isbn="9788954618984", language=Language.objects.filter(name__icontains="한국")[0])
        Author.objects.create(first_name="난도", last_name="김", date_of_birth=datetime.date(1965, 9, 20))
        Author.objects.create(first_name="미영", last_name="전", date_of_birth=datetime.date(1972, 2, 11))
        Genre.objects.create(name="시")
        Genre.objects.create(name="에세이")
        Genre.objects.create(name="경제전망")
        Genre.objects.create(name="경영전략")
        Book.objects.get(title__icontains="트렌드").author.add(Author.objects.get(first_name__icontains="난도"))
        Book.objects.get(title__icontains="트렌드").author.add(Author.objects.get(first_name__icontains="미영"))
        Book.objects.get(title__icontains="트렌드").genre.add(Genre.objects.get(name__icontains="경제"))
        Book.objects.get(title__icontains="트렌드").genre.add(Genre.objects.get(name__icontains="경영"))
        Book.objects.get(title__icontains="천 번을").author.add(Author.objects.get(first_name__icontains="난도"))
        Book.objects.get(title__icontains="천 번을").genre.add(Genre.objects.get(name__icontains="시"))
        Book.objects.get(title__icontains="천 번을").genre.add(Genre.objects.get(name__icontains="에세이"))
        BookInstance.objects.create(
            book=Book.objects.get(title__icontains="트렌드"),
            summary="트렌드를 알아보세요!",
            rent_availability=True,
            donate_availability=False,
            location_longitude=140.15568423,
            location_latitude=40.56198156
        )

    def test_db_connected(self):
        """are the relations connected well on many to many fields?"""
        book_1 = Book.objects.get(title__icontains="트렌드")
        book_2 = Book.objects.get(title__icontains="천 번을")
        book_instance=BookInstance.objects.filter(book=book_1)[0]
        self.assertEqual(book_1.author.all()[0].first_name, "난도")
        self.assertEqual(book_1.author.all()[1].first_name, "미영")
        self.assertEqual(book_1.genre.all()[0].name, "경제전망")
        self.assertEqual(book_1.genre.all()[1].name, "경영전략")
        self.assertEqual(book_2.author.all()[0].first_name, "난도")
        self.assertEqual(book_2.genre.all()[0].name, "시")
        self.assertEqual(book_2.genre.all()[1].name, "에세이")
        self.assertEqual(book_instance.book.title, "트렌드 코리아 2020")

    def test_home_view_sends_book_instances(self):
        url = reverse('openbooks:home') + '?category=%EB%8F%84%EC%84%9C%EB%AA%85&content=%ED%8A%B8%EB%A0%8C%EB%93%9C+%EC%BD%94%EB%A6%AC%EC%95%84+2020'
        response = self.client.get(url)
        self.assertEqual(response.context['ordered_books'][0], BookInstance.objects.filter(book__title__icontains='트렌드')[0])

    def test_home_view_distance_ordered(self):
        book_distance_2 = BookInstance.objects.create(
            book=Book.objects.get(title__icontains="트렌드"),
            summary="2.대림미술관",
            rent_availability=True,
            donate_availability=False,
            location_latitude=37.577991,
            location_longitude=126.973204
        )
        book_distance_1 = BookInstance.objects.create(
            book=Book.objects.get(title__icontains="트렌드"),
            summary="1.미국대사관",
            rent_availability=True,
            donate_availability=False,
            location_latitude=37.573297,
            location_longitude=126.978225
        )
        book_distance_3 = BookInstance.objects.create(
            book=Book.objects.get(title__icontains="트렌드"),
            summary="3.고려사이버대학교",
            rent_availability=True,
            donate_availability=False,
            location_latitude=37.586907,
            location_longitude=126.986630
        )
        url = reverse('openbooks:home') + '?category=%EB%8F%84%EC%84%9C%EB%AA%85&content=%ED%8A%B8%EB%A0%8C%EB%93%9C+%EC%BD%94%EB%A6%AC%EC%95%84+2020'
        response = self.client.get(url)
        for indibook in response.context['ordered_books']: print(indibook.summary)
        self.assertEqual(response.context['ordered_books'][0], BookInstance.objects.filter(summary__icontains='1')[0])
        self.assertEqual(response.context['ordered_books'][1], BookInstance.objects.filter(summary__icontains='2')[0])
        self.assertEqual(response.context['ordered_books'][2], BookInstance.objects.filter(summary__icontains='3')[0])
