from django.contrib import admin

# Register your models here.

from .models import Item #why .models??

class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'amount']

admin.site.register(Item, ItemAdmin) #registers item with model. 
    