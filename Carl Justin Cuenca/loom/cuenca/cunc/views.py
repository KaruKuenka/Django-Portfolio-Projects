from django.shortcuts import render
from django.http import HttpResponse
from .models import dataClass
# Create your views here.


def show_data(request): 
    dataClassData = dataClass.objects.all()

    return render(request, 'home.html', {'dataClass':dataClassData})