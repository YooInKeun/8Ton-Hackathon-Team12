from django.shortcuts import render
from openbooks.models import BookInstance
import math

def home(request):
    books_unordered = BookInstance.objects.all()
    context = {}
    for book in books_unordered:
        context[book.id] = math.sqrt(math.pow(book.location_longitude, 2) + math.pow(book.location_latitude, 2))
    context = { 'books_ordered': sorted(context) }
    return render(request, 'openbooks_index.html', context)

