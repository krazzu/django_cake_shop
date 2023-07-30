from django.shortcuts import render, redirect
from .forms import OrderForm
from cart.cart import Cart
from .models import OrderItem


def order(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            # создаем объект Order
            order1 = form.save(commit=False)
            if cart.get_total_price() > 0:
                order1.order_total = cart.get_total_price()
                order1.save()
                for item in cart:
                    order_item = OrderItem(order=order1.id, product=item['product'], quantity=item['quantity'])
                    order_item.save()
                # очищаем корзину
                cart.clear()

                # перенаправляем на страницу оплаты
                return redirect('https://qiwi.com/withdraw')
            else:
                return redirect('http://127.0.0.1:8000/catalog')
    else:
        form = OrderForm()
    return render(request, 'order/order.html', {'cart': cart, 'form': form})
