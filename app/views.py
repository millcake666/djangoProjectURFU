from django.shortcuts import render
from . import models
from .utils import parse_data


def home_page(request):
    profession = models.Profession.objects.all()

    return render(request, 'app/home.html', context={'profession': profession})


def get_page_info(page):
    try:
        model_page = models.Page.objects.get(title=page)
    except Exception as e:
        return

    csv_files = models.Table.objects.filter(page_id=model_page.id).all()
    charts = models.Image.objects.filter(page_id=model_page.id).all()

    tables = []
    for file in csv_files:
        table = parse_data(file.file.path)
        tables.append(table)

    return {'tables': tables, 'charts': charts}


def demand(request):
    page = 'Востребованность'

    context = get_page_info(page)
    if context is None:
        return render(request, 'app/notfound.html', context=dict(page=page))

    return render(request, 'app/demand.html', context=context)


def geo(request):
    page = 'География'
    context = get_page_info(page)
    if context is None:
        return render(request, 'app/notfound.html', context=dict(page=page))

    return render(request, 'app/demand.html', context=context)


def skills(request):
    page = 'Навыки'
    context = get_page_info(page)
    if context is None:
        return render(request, 'app/notfound.html', context=dict(page=page))
    return render(request, 'app/demand.html', context=context)


def latest_vacancies(request):
    return render(request, 'app/latest_vacancies.html', context={})
