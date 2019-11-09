from django.shortcuts import render

def home(request):
    return render(request, 'openbooks_index.html')