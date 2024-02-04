from django.urls import path
from . import views

urlpatterns = [

    path('', views.cars),
    
    path("<int:pk>/", views.car_detail, name="car_detail"),

]