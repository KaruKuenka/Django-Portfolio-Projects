from django.shortcuts import render
from django.http import HttpResponse
from .models import dataClassas, Skill, Projects
# Create your views here.


def show_data(request): 
    dataClassData = dataClassas.objects.all()

    return render(request, 'home.html', {'dataClassas':dataClassData})

def portfolio_view(request):
    skills = Skill.objects.all()
    projects = Projects.objects.all()
    context = {
        'name': 'Cuenca, Carl Justin D.',
        'title': 'IT student',
        'about': 'Brief intro: Passionate about hardware related in IT. \nExperienced in fixing computers',
        'skills': skills,
        'projects': projects,
        'email': 'carlcuenca092423@gmail.com',
        'linkedln': 'Not Available',
        'number': '0995-876-4828'
    }

    return render(request, 'portfolio.html', context) 