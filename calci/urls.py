# from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('cal/', views.calculate,name = 'calculate'),
    # cal/ = this can be any name
    # views.calculate = only view name which is present in [views.py] file
    # This gives the route a name, so it can be referred to in templates using {% url 'calculate' %}.
    

]
