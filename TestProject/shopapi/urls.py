from django.urls import path
from . import views

app_name = 'shopapi'

urlpatterns = [
    path('products/', views.index, name='index'),
    path('products/add/', views.add_product, name='add_product'),
    path('products/add-cbv/', views.AddProductView.as_view(), name='add_product_cbv'),
    path('products-cbv/', views.ProductsView.as_view(), name='products_cbv')
]