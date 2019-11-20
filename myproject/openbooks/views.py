from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.utils import timezone
import json
import math
import operator

def home(request):
    """ 현제 위치를 반영해야하는데, """
    local_lat = 37.571605
    local_long = 126.976549
    """ 반영 안하고 있죠^^ 수정이 급급 """
    books_instances_unordered = []

    if request.GET.get('content') != None:
        if request.GET['category'] == '도서명':
            books_unordered = [
                one_book for one_book in Book.objects.filter(
                    title__icontains=request.GET.get('content')
                )
            ]
            books_instances_unordered = BookInstance.objects.filter(
                book__in=books_unordered
            )
        elif request.GET['category'] == '저자명':
            books_unordered = [
                one_author for one_author in Author.objects.filter(
                    first_name__icontains=request.GET.get('content')
                )
            ]
            books_instances_unordered = BookInstance.objects.filter(
                book__in=books_unordered
            )
    else:
        if(request.method == 'GET'):
        books_instances_unordered = BookInstance.objects.all()

    books_tobesorted = {}
    for book_instance in books_instances_unordered:
        books_tobesorted[book_instance.id] = math.sqrt(
            math.pow(math.fabs(book_instance.location_longitude) - local_long, 2)
            + math.pow(math.fabs(book_instance.location_latitude) - local_lat, 2)
        )
    books_sorted = sorted(books_tobesorted.items(), key=lambda element: element[1])
    books_sorted = books_sorted[:10]
    # books_sorted becomes a list of tuples, nicely sorted by distances
    book_context = {}
    context = {}
    for idx, books_UID in enumerate(books_sorted):
        bookinstance = get_object_or_404(BookInstance, id=books_UID[0])
        book_context[idx] = bookinstance
    book_context = list(book_context.values())
    context['ordered_books'] = book_context
    return render(request, 'openbooks_index.html', context)


def register(request):
    return render(request, 'register.html')

def create(request):

    bookinstance = BookInstance()
    bookinstance.book = Book.objects.get(title=request.POST.get('title'))
    bookinstance.summary = request.POST.get('summary')
    if request.POST.get('rent_availability') == 'True':
        bookinstance.rent_availability = True
        bookinstance.donate_availability = False
    elif request.POST.get('donate_availability') == 'True':
        bookinstance.rent_availability = False
        bookinstance.donate_availability = True
    bookinstance.location_longitude = 127.48590468
    bookinstance.location_latitude = 38.15485658
    bookinstance.save()
    books = BookInstance.objects.all()

    return render(request, 'register.html', {'books' : books})

def post(request):
    if request.method == 'POST':
        lonlat=json.loads(request.body)
        print('경도: ' + str(lonlat['lon'])) # 세로선
        print('위도: ' + str(lonlat['lat'])) # 가로선
    return redirect('home')
