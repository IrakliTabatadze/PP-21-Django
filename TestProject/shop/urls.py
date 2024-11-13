from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('product/add/', views.add_product, name='add_product'),
    path('product/detail/<int:pk>/', views.detail_product, name='detail_product')
]