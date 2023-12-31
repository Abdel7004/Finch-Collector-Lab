from django.db import models
# at top of file
import time

# Create your models here.

class Manufacture(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    bio = models.TextField(max_length=500)
    verified_manufacture = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

# below Manufacture Model

class Car(models.Model):

    title = models.CharField(max_length=150)
    hp = models.IntegerField(default=0)
    manufacture = models.ForeignKey(Manufacture, on_delete=models.CASCADE, related_name="cars")

    def __str__(self):
        return self.title

class Favorite(models.Model):

    title = models.CharField(max_length=150)
    # this is going to create the many to many relationship and join table
    cars = models.ManyToManyField(Car)

    def __str__(self):
        return self.title
