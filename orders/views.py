from django.shortcuts import render
from cart.cart import Cart
from orders.forms import OrderCreateForm
from orders.models import OrderItem


# View > Handle Form & Create Order
def order_create(request):
    # Get info of current cart from session.
    cart = Cart(request)
    if request.method == 'POST':
        # Request Payment Form
        form = OrderCreateForm(request.POST)
        # If all data are valid - Save it
        if form.is_valid():
            order = form.save() # if valid - create new order in DB.
            # Loop over the order and each product, price, and quantity of item.
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],
                                         price=item['price'], quantity=item['quantity'])
            cart.clear()
        return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})


