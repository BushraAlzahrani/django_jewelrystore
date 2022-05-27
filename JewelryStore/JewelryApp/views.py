from django.shortcuts import render
from .models import *

def home(request):
    return render(request, 'home.html')


def jewelries(request):
    j_all_list = Jewelry.objects.all()
    return render(request, 'jewelries.html', {'j_list': j_all_list})

def jewlry_page(request):
    pass