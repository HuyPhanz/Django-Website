from django.shortcuts import render

from store.models import Product


# Create your views here.
def store(request):
  context = {'Products': Product.objects.all().order_by("-date")}
  return render(request, 'store/store.html', context)


def cart(request):
  context = {}
  return render(request, 'store/cart.html', context)


def checkout(request):
  context = {}
  return render(request, 'store/checkout.html', context)
