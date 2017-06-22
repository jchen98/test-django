from django.shortcuts import render
from django.http import HttpResponse #response object that views returns
from django.http import Http404 #returns 404 page

from inventory.models import Item #
# Create your views here.

def index(request):
    items = Item.objects.exclude(amount=0)
    return render(request, 'inventory/index.html', {
        'items': items,
    }) #creates http response and connects to a template. 
    
def item_detail(request, id): #this is from before, name group for id
    try:
        item = Item.objects.get(id=id)
    except Item.DoesNotExist:
        raise Http404('this item does not exist')
    return render(request, 'inventory/item_detail.html', {
        'item': item,
    })
    
