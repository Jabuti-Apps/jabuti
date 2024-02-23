from django.urls import path
from . import views

urlpatterns = [
    path("", views.autorizacao, name="autorizacao"),
    path("signup/", views.signup, name="signup"),
    path('criar/', views.criar, name="create-user"),
    path("login/", views.login, name="login"),
]
