from django.db import models

class Item(models.Model): #this inherits from models.Model
    #these are class attributes
    title = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.IntegerField()
    
    #this will be called inventory_item.