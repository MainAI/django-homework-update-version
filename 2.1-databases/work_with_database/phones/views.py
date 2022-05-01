from django.shortcuts import render, redirect, get_object_or_404
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    product = Phone.objects.all()
    SORT_MAP = {
        'name': 'name',
        'min_price': 'price',
        'max_price': '-price',
    }
    sort_by = request.GET.get('sort')
    if sort_by:
        product = product.order_by(SORT_MAP[sort_by])
    template = 'catalog.html'
    context = {'phones': product}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phone': get_object_or_404(Phone, slug=slug)}
    return render(request, template, context)
