from django.shortcuts import render

# Create your views here.
from .models import CartItem
from django.views.generic import TemplateView, ListView

class CartView(ListView):
    model = CartItem
    template_name = 'cart/cart.html'
    context_object_name = 'cart_items'

    def get_queryset(self):
        return CartItem.objects.filter( user = self.request.user)

