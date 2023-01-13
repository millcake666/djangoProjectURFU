from django.shortcuts import render
from . import models
from .utils import parse_data


def home_page(request):
    profession = models.Profession.objects.all()
    return render(request, 'app/home.html', context={'profession': profession})


def detail(request):
    professions = models.Profession.objects.all()
    tables = list()
    for profession in professions:
        files = models.File.objects.filter(profession_id=profession.id).all()
        for file in files:
            tables.append(parse_data(file.file.path))
    return render(request, 'app/detail.html', context={'tables': tables})
