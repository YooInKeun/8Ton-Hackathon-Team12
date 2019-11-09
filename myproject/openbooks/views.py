from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.utils import timezone
import json
import math
import operator

def home(request):
    local_long =0
    local_lat=0
    if request.GET.get('content') != None:
        if request.GET['category'] == '도서명':
            books_unordered = BookInstance.objects.filter(book=Book.objects.get(title__icontains=request.GET.get('content')))[:10]
        elif request.GET['category'] == '저자명':
            books_unordered = BookInstance.objects.filter(book=Book.objects.get(author=Author.objects.get(last_name__icontains=request.GET.get('content'))))[:10]
    else:
        print(1)
        if(request.method == 'GET'):
            local_long = 127.15568423
            local_lat = 38.56198156
        books_unordered = BookInstance.objects.all()[:10]

    books_tobesorted = {}
    for book in books_unordered:
        books_tobesorted[book.id] = math.sqrt(
            math.pow(math.fabs(book.location_longitude) - local_long, 2)
            + math.pow(math.fabs(book.location_latitude) - local_lat, 2)
        )
    books_tobesorted = sorted(books_tobesorted.items(), key=operator.itemgetter(1))
    book_context = {}
    context = {}
    for idx, books_UID in enumerate(books_tobesorted):
        bookinstance = BookInstance.objects.get(id=books_UID[0])
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
