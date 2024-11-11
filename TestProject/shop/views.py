from django.shortcuts import render, redirect
from .models import Category, Product
from .forms import ProductForm

def index(request):
    product_name = request.GET.get('product_name')
    category = request.GET.getlist('category')

    if product_name:
        products = Product.objects.filter(name__icontains=product_name)
    elif category:
        products = Product.objects.filter(category__in=category)
    else:
        products = Product.objects.all()


    categories = Category.objects.all()
    category_by_type = {}

    for category in categories:
        category_type = category.category_type
        if category_type not in category_by_type:
            category_by_type[category_type] = []
        category_by_type[category_type].append(category)

    print(category_by_type)


    return render(request, 'index.html', {'products': products, 'categories_by_type': category_by_type})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            form.save_m2m()
            return redirect('shop:index')
    else:
        form = ProductForm()
        return render(request, 'add_product.html', {'form': form})