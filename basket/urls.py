from django.urls import path

from . import views

app_name = 'basket'

urlpatterns = [
    path('', views.view_basket, name='view_basket'),
    path("add", views.add_to_basket, name='add_to_basket'),
    path('remove/', views.remove_from_basket, name='remove_from_basket'),
]