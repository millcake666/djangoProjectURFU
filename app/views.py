from django.shortcuts import render
from . import models
from .utils import parse_data


def home_page(request):
    profession = models.Profession.objects.all()
    return render(request, 'app/home.html', context={'profession': profession})


def demand(request):
    page = 'Востребованность'
    try:
        model_page = models.Page.objects.get(title=page)
    except Exception as e:
        return render(request, 'app/notfound.html', context=dict(page=page))

    csv_files = models.Table.objects.filter(page_id=model_page.id).all()
    charts = models.Image.objects.filter(page_id=model_page.id).all()

    tables = []
    for file in csv_files:
        table = parse_data(file.file.path)
        tables.append(table)

    return render(request, 'app/demand.html', context={'tables': tables, 'charts': charts})


def geo(request):
    return render(request, 'app/geo.html', context={})


def skills(request):
    return render(request, 'app/skills.html', context={})


def latest_vacancies(request):
    return render(request, 'app/latest_vacancies.html', context={})
