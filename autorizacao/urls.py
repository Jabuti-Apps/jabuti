from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path('criar/', views.criar, name="create_user"),
    path("login/", views.submit_login, name="submit_login"),
    path("logout/", views.logout_user, name="logout"),
    path("calendar/", views.calendar, name="calendar"),
    
]
