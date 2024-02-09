from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, CartItem
from django.http import HttpResponse

def product_list(request):
    products = Product.objects.all()
    print(products)  # Debugging: Print the products retrieved
    return render(request, 'product_list.html', {'products': products})

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('product_list') 

def view_cart(request):
    cart_items = CartItem.objects.all()
    return render(request, 'cart.html', {'cart_items': cart_items})


def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, pk=cart_item_id)
    cart_item.delete()
    return redirect('view_cart')

def update_quantity(request):
    if request.method == 'POST':
        cart_item_id = request.POST.get('cart_item_id')
        new_quantity = int(request.POST.get('new_quantity'))
        try:
            cart_item = CartItem.objects.get(id=cart_item_id)
            cart_item.quantity = new_quantity
            cart_item.save()
            return HttpResponse('Quantity updated successfully.')
        except CartItem.DoesNotExist:
            return HttpResponse('Cart item not found.')
    else:
        return HttpResponse('Invalid request method.')
