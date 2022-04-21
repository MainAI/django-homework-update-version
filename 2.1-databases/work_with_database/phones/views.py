from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    product = Phone.objects.all()
    sort_by = request.GET.get('sort')
    if sort_by == 'name':
        product = Phone.objects.all().order_by('name')
    elif sort_by == 'min_price':
        product = Phone.objects.all().order_by('price')
    elif sort_by == 'max_price':
        product = Phone.objects.all().order_by('-price')
    template = 'catalog.html'
    context = {'phones': product}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phone': Phone.objects.get(slug=slug)}
    return render(request, template, context)
