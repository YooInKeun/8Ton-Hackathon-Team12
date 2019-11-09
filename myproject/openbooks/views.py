from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.utils import timezone
import json
import math


def home(request):

    if(request.method == 'GET'):
        local_long = request.GET['longitude']
        local_lat = request.GET['latitude']
    books_unordered = BookInstance.objects.all()
    books_tobesorted = {}
    for book in books_unordered:
        books_tobesorted[book.id] = math.sqrt(
            math.pow(math.fabs(book.location_longitude) - local_long, 2)
            + math.pow(math.fabs(book.location_latitude) - local_lat, 2)
        )
    books_tobesorted = sorted(books_tobesorted)
    context = {}
    for books_UID in books_tobesorted:
        context['books_sorted'] = get_object_or_404(BookInstance, id=books_UID)
    return render(request, 'openbooks_index.html', context)


def register(request):
    return render(request, 'register.html')

def create(request):

    bookinstance = BookInstance()
    bookinstance.book = Book.objects.get(title=request.POST.get('book'))
    bookinstance.summary = request.POST.get('summary')
    bookinstance.rent_availability = request.POST.get('rent_availability')
    bookinstance.donate_availability = reques.POST.get('donate_availability')
    bookinstance.location_longitude = request.POST.get('location_longitude')
    bookinstance.location_latitude = request.POST.get('location_latitude')
    bookinstance.save()
    books = BookInstance.objects.all()
    
    return render(request, 'register.html', {'books' : books})

def post(request):
    if request.method == 'POST':
        lonlat=json.loads(request.body)
        print('경도: ' + str(lonlat['lon'])) # 세로선
        print('위도: ' + str(lonlat['lat'])) # 가로선
    return redirect('home')
