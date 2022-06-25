from django.shortcuts import render
from .models import Info
# Create your views here.


def home(request):
    InfoPics = Info.objects
    return render(request, 'home.html', {'InfoPics': InfoPics})


def address(request):
    return render(request, 'address.html')


def contact(request):
    return render(request, 'contact.html')
