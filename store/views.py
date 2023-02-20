from django.shortcuts import render

from .models import Category, Product


def categories(requests):
    return {
        'categories': Category.objects.all(),
    }


def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})
