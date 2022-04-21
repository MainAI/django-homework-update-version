from django.core.paginator import Paginator
from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
import csv


station_list = []
with open(settings.BUS_STATION_CSV, newline='', encoding='UTF-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        station_list.append({'Name': row['Name'], 'Street': row['Street'], 'District': row['District']})


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    paginator = Paginator(station_list, 10)
    current_page = int(request.GET.get('page', 1))
    page = paginator.get_page(current_page)

    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)

