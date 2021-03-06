from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

# Create your views here.
def home(request):
    items = Item.objects.all().order_by('created')
    return render(request, 'inventory/index.html', {'items':items})

def product_detail(request,slug):
    # return HttpResponse("Success")
    product = Item.objects.get(slug=slug)
    return render(request, 'inventory/details.html', {'product':product})