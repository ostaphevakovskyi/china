from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'cafe/home.html', {})
def about(request):
    return render(request, 'cafe/about.html', {})
    
