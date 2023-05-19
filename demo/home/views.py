from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
   return render(request , "index.html")

def animals(request):
   return render(request , "animals.html")

def forest(request):
   return render(request , "forest.html")

def water(request):
   return render(request , "water.html")

def indoor(request):
   return render(request , "indoor.html")

def outdoor(request):
   return render(request , "indoor.html")

def contact(request):
   return render(request , "contact.html")

