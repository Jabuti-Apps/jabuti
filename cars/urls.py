from django.urls import path
from . import views

urlpatterns = [

    path('', views.cars),

    path("<int:id>/", views.car_detail, name="car_detail"),

    path('disponiveis/', views.disponiveis, name='disponiveis'),

]