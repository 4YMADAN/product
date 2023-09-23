from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Lesson,Owner


def index(request):
    return render(request, "lessons/index.html")
def product(request):
    return render(request, "lessons/about.html")

def registration(request):
    return render(request, "lessons/registration.html")