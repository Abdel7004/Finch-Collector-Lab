from django.contrib import admin
from .models import Manufacture, Car, Favorite # import the Artist model from models.py
# Register your models here.

admin.site.register(Manufacture) # this line will add the model to the admin panel
admin.site.register(Car) # this line will add the model to the admin panel
admin.site.register(Favorite) # this line will add the model to the admin panel