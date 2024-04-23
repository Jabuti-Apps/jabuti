from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path('cadastro/', views.cadastro, name="cadastro"),
    path("login/", views.submit_login, name="submit_login"),
    path("logout/", views.logout_user, name="logout"),
    path("calendar/", views.calendar, name="calendar"),
    path("funcionarios/", views.funcionarios, name="funcionarios"),
]
