from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.products_all, name='products_all'),
    path('search/<slug:slug>/', views.product_detail, name='product_detail'),
    path('books/<slug:category_slug>/', views.category_list, name='category_list'),
]