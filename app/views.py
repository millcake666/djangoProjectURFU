from django.shortcuts import render
from . import models
from .utils import parse_data


def home_page(request):
    profession = models.Profession.objects.all()
    return render(request, 'app/home.html', context={'profession': profession})


def demand(request):
    professions = models.Profession.objects.all()
    tables = list()
    for profession in professions:
        files = models.FileProfession.objects.filter(profession_id=profession.id).all()
        for file in files:
            tables.append(parse_data(file.file.path))
    return render(request, 'app/demand.html', context={'tables': tables})


def geo(request):
    return render(request, 'app/geo.html', context={})


def skills(request):
    return render(request, 'app/skills.html', context={})


def latest_vacancies(request):
    return render(request, 'app/latest_vacancies.html', context={})
