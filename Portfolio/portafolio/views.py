from django.shortcuts import render

# Create your views here.
from portafolio.models import Project


def portafolio(request):
    proyectos = Project.objects.all()
    return render(request, 'Portafolio.html', {'proyectos': proyectos})
