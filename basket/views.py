from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect

from store.models import Product
from .basket import Basket


def refresh_view(request):
    return redirect(request.META.get('HTTP_REFERER'))

def add_to_basket(request):
    basket = Basket(request)
    if request.method == 'POST':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=product_qty)
        return redirect(request.META.get('HTTP_REFERER'))

def remove_from_basket(request):
    basket = Basket(request)
    if request.method == 'POST':
        product_id = int(request.POST.get('productid'))
        product = get_object_or_404(Product, id=product_id)
        basket.remove(product)
        return redirect(request.META.get('HTTP_REFERER'))

def view_basket(request):
    basket = Basket(request)
    basket_items = []
    for item in basket:
        product = item['product']
        quantity = item['qty']
        total_price = item['total_price']
        basket_items.append({
            'product': product,
            'quantity': quantity,
            'total_price': total_price
        })
    context = {'basket_items': basket_items}
    return render(request, 'store/basket/basket.html', context)
    

