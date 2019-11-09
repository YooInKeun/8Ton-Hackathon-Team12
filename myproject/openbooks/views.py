from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.utils import timezone
import json

def home(request):
    return render(request, 'openbooks_index.html')

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