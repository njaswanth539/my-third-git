from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def first(request):
    return HttpResponse('jaswanth is smartboy')

def second(request):
    return HttpResponse ('<h1><marqee>jasu is nickname of jaswanth</marquee></h1>')
    
    
