from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'mainapp'

urlpatterns = [
    path('',views.home,name='home'),
    path('user/',views.userPage,name='userPage'), #userPage
    path('product/',views.fooditem,name='fooditem'),
    path('createfooditem/',views.createfooditem,name='createfooditem'),
    path('register/',views.registerPage,name='register'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('addFooditem/',views.addFooditem,name='addFooditem'),

]