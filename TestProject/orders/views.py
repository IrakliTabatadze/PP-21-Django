from django.shortcuts import render, redirect
from .models import Cart, CartItem
from shop.models import Product
from django.contrib.auth.decorators import login_required
from django.views.generic import View, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required(login_url='/users/login')
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_items = CartItem.objects.filter(cart=cart)

    total_amount = sum(cart_item.total for cart_item in cart_items)


    return render(request, 'cart.html', {'cart_items': cart_items, 'total_amount': total_amount})


@login_required(login_url='/users/login')
def add_cart_item(request, pk):

    product = Product.objects.get(pk=pk)

    cart, created = Cart.objects.get_or_create(user=request.user)
    print(f'Product Stock: {product.stock}')
    if product.stock > 0:
        cart_item, cart_item_created = CartItem.objects.get_or_create(cart=cart, product=product)
        print(f'Cart Item Created: {cart_item_created}')
        if not cart_item_created:
            print(f'CartItem Not Created')
            cart_item.quantity += 1
        elif cart_item_created:
            print(f'CartItem Created')
            cart_item.quantity = 1
        cart_item.save()

    return redirect(request.META.get('HTTP_REFERER'))


class AddCartItem(LoginRequiredMixin, View):

    @staticmethod
    def get(request, pk):
        product = Product.objects.get(pk=pk)

        cart, created = Cart.objects.get_or_create(user=request.user)
        print(f'Product Stock: {product.stock}')
        if product.stock > 0:
            cart_item, cart_item_created = CartItem.objects.get_or_create(cart=cart, product=product)
            print(f'Cart Item Created: {cart_item_created}')
            if not cart_item_created:
                print(f'CartItem Not Created')
                cart_item.quantity += 1
            elif cart_item_created:
                print(f'CartItem Created')
                cart_item.quantity = 1
            cart_item.save()

        return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/users/login')
def update_cart_item(request, pk):
    if request.method == 'POST':
        cart_item = CartItem.objects.get(pk=pk)

        new_quantity = int(request.POST.get('quantity'))

        if new_quantity == 0:
            cart_item.delete()

        elif new_quantity <= cart_item.product.stock:
            cart_item.quantity = new_quantity
            cart_item.save()

    return redirect(request.META.get('HTTP_REFERER'))

class UpdateCartItemView(View):

    @staticmethod
    def post(request, pk):
        cart_item = CartItem.objects.get(pk=pk)

        new_quantity = int(request.POST.get('quantity'))

        if new_quantity == 0:
            cart_item.delete()

        elif new_quantity <= cart_item.product.stock:
            cart_item.quantity = new_quantity
            cart_item.save()

        return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/users/login')
def delete_cart_item(request, pk):
    cart_item = CartItem.objects.get(pk=pk)

    cart_item.delete()

    return redirect(request.META.get('HTTP_REFERER'))


class DeleteCartItemView(DeleteView):
    model = CartItem
    success_url = reverse_lazy('orders:cart')