from django.shortcuts import render, redirect
from .models import Category, Product
from .forms import ProductForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required

def index(request):
    product_name = request.GET.get('product_name')
    category = request.GET.getlist('category')

    print("Categories: ", category)

    if product_name:
        products = Product.objects.filter(name__icontains=product_name)
    elif category:
        products = Product.objects.filter(category__in=category)
    else:
        products = Product.objects.all()

    paginator = Paginator(products, 8)

    try:
        page_number = request.GET.get('page')
        products = paginator.page(page_number)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    categories = Category.objects.all()
    category_by_type = {}

    for category in categories:
        category_type = category.category_type
        if category_type not in category_by_type:
            category_by_type[category_type] = []
        category_by_type[category_type].append(category)

    print(category_by_type)

    return render(request, 'index.html', {'products': products, 'categories_by_type': category_by_type})

@login_required(login_url='/users/login/')
def detail_product(request, pk):
    product = Product.objects.get(pk=pk)

    related_products = Product.objects.filter(category__in=product.category.all()).exclude(id=product.id)[:4]

    return render(request, 'detail_product.html', {'product': product, 'related_products': related_products})


def add_product(request):
    if request.user.has_perm('shop.add_product'):
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
    else:
        return redirect('shop:index')