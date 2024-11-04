from django.shortcuts import render, HttpResponse
from django.db import connection
from .models import Product, Supplier
from django.db.models import Q

global_var = "hello world"

def index(request):
    # cursor = connection.cursor()
    # cursor.execute('select * from products')
    # print(cursor.fetchall())

    # product = Product.objects.create(name='Asus Vivobook', description='Asus new laptop', price=1555.55)

    # product = Product()
    # product.name = 'HP G255'
    # product.price = 1444.44
    # product.save()

    # products = Product.objects.all()
    # print(products)

    # products = Product.objects.filter(name__icontains='pro').first()
    # print(products)

    # products = Product.objects.filter(name__in=['Macbook Pro', 'HP G255']).all()
    # print(products)

    # product = Product.objects.get(pk=1)
    # print(product)

    # products = Product.objects.filter(Q(name__icontains='pro') | Q(name__icontains='hp'))
    # print(products)

    # products = Product.objects.filter(~Q(name__icontains='hp') & Q(price__gte=1000))
    # print(products)

    # product = Product.objects.get(pk=1)
    # product.price = 2500
    # product.save()
    # print(product)

    # product = Product.objects.get(pk=4)
    # product.delete()


    # suppliers = Supplier.objects.all()
    # for supplier in suppliers:
    #     print(supplier.name, supplier.product.name)

    # suppliers = Supplier.objects.filter(product__name__icontains='G255').first()
    # print(suppliers)

    supplier = Supplier.objects.select_related('product').all()
    print(supplier)

    return HttpResponse('<h1>Hello From Views.py</h1>')

def test(request):
    return render(request, 'testhtml.html', {'variable': global_var})


def test2(request):
    return render(request, 'test2.html')