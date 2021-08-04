from django.urls import path
from . import views

app_name = "mainapp"


urlpatterns = [
    path("", views.home, name="home"),
    path("register", views.register_request, name="register")
]