from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('index-cbv/', views.IndexView.as_view(), name='index-cbv'),
    path('product/add/', views.add_product, name='add_product'),
    path('product-cbv/add/', views.AddProductView.as_view(), name='add_product_cbv'),
    path('product/detail/<int:pk>/', views.detail_product, name='detail_product'),
    path('product-cbv/detail/<int:pk>/', views.ProductDetailView.as_view(), name='detail_product_cbv')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
