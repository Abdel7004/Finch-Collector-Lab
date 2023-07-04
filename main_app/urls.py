from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"), # <- here we have added the new path
    path('about/', views.About.as_view(), name="about"), # <- new route
    path('manufacture/', views.ManufactureList.as_view(), name="manufacture_list"),
    path('cars/', views.CarList.as_view(), name="car_list"),
      # Here is our new route
    path('manufacture/new/', views.ManufactureCreate.as_view(), name="manufacture_create"),
     # Our new Route including the pk param
    path('manufactures/<int:pk>/', views.ManufactureDetail.as_view(), name="manufacture_detail"),
    # Our new Route including the pk param
    path('manufactures/<int:pk>/update',views.ManufactureUpdate.as_view(), name="manufacture_update"),
    # Our new Route including the pk param
    path('manufactures/<int:pk>/delete',views.ManufactureDelete.as_view(), name="manufacture_delete"),
    path('manufactures/<int:pk>/cars/new/', views.CarCreate.as_view(), name="car_create"),
    # Here is our new url
    path('favorites/<int:pk>/cars/<int:car_pk>/', views.FavoriteCarAssoc.as_view(), name="favorite_car_assoc"),
]