from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'purrfectpets/home.html')

def aboutus(request):
    return render(request, 'purrfectpets/aboutus.html')

def popular_pets(request):
    return render(request, 'purrfectpets/popular_pets.html')

def categories(request):
    return render(request, 'purrfectpets/categories.html')

def dogs(request):
    return render(request, 'purrfectpets/dogs.html')
def cats(request):
    return render(request, 'purrfectpets/cats.html')
def fish(request):
    return render(request, 'purrfectpets/fish.html')
def reptiles(request):
    return render(request, 'purrfectpets/reptiles.html')
def rodents(request):
    return render(request, 'purrfectpets/rodents.html')
def other(request):
    return render(request, 'purrfectpets/other.html')