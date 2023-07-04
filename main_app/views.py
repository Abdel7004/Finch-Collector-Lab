from django.shortcuts import render
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
# import models
from .models import Manufacture, Car, Favorite
# This will import the class we are extending 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# after our other imports 
from django.views.generic import DetailView
# at the top of the file import reverse 
from django.urls import reverse
from django.shortcuts import redirect
from django.views import View # <- View class to handle requests


# Create your views here.

class Home(TemplateView):
    template_name = "home.html"
    # Here we have added the playlists as context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["favorites"] = Favorite.objects.all()
        return context


#...
class About(TemplateView):
    template_name = "about.html"

class ManufactureList(TemplateView):
    template_name = "manufacture_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
            # to get the query parameter we have to acccess it in the request.GET dictionary object        
        name = self.request.GET.get("name")
        # If a query exists we will filter by name 
        if name != None:
            # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param
            context["manufactures"] = Manufacture.objects.filter(name__icontains=name)
        else:
            context["manufactures"] = Manufacture.objects.all()
            context["header"] = "Top Manufactures"
        return context

class CarList(TemplateView):
    template_name = "car_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cars"] = cars # this is where we add the key into our context object for the view to use
        return context

class ManufactureCreate(CreateView):
    model = Manufacture
    fields = ['name', 'img', 'bio', 'verified_manufacture']
    template_name = "manufacture_create.html"
    def get_success_url(self):
        return reverse('manufacture_detail', kwargs={'pk': self.object.pk})

class ManufactureDetail(DetailView):
    model = Manufacture
    template_name = "manufacture_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["favorites"] = Favorite.objects.all()
        return context

class ManufactureUpdate(UpdateView):
    model = Manufacture
    fields = ['name', 'img', 'bio', 'verified_manufacture']
    template_name = "manufacture_update.html"
    def get_success_url(self):
        return reverse('manufacture_detail', kwargs={'pk': self.object.pk})

class ManufactureDelete(DeleteView):
    model = Manufacture
    template_name = "manufacture_delete_confirmation.html"
    success_url = "/manufacture/"

class CarCreate(View):

    def post(self, request, pk):
        title = request.POST.get("title")
        hp = request.POST.get("length")
        manufacture = Manufacture.objects.get(pk=pk)
        Car.objects.create(title=title, hp=hp, manufacture=manufacture)
        return redirect('manufacture_detail', pk=pk)

class FavoriteCarAssoc(View):

    def get(self, request, pk, car_pk):
        # get the query param from the url
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            # get the playlist by the id and
            # remove from the join table the given song_id
            Favorite.objects.get(pk=pk).cars.remove(car_pk)
        if assoc == "add":
            # get the playlist by the id and
            # add to the join table the given song_id
            Favorite.objects.get(pk=pk).cars.add(car_pk)
        return redirect('home')
