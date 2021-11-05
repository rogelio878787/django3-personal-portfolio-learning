from django.shortcuts import render, get_list_or_404, redirect
from django.views.generic import ListView,DetailView
from .models import Item, OrderItem, Order
from django.utils import timezone



from django.contrib.auth.forms import UserCreationForm





class ProductListView(ListView):
    model = Item
    template_name = 'home-page.html'


class ProductDetailView(DetailView):
    model = Item
    template_name = 'product-page.html'



def add_to_cart(request, slug):
    item = get_list_or_404(slug=slug)
    order_item = OrderItem.objects.create(item = item)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]

        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity +=1
            order_item.save()

    else:
        order_date = timezone.now
        order = Order.objects.create(user=request.user, order_date=order_date)
        order.items.add(order_item)
    return redirect('products',slug=slug)






def checkout(request):
    return render(request, 'checkout-page.html',{})






def login_view(request):
    return render(request,'login.html', {})