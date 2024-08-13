from django.contrib import admin
from django.urls import path
from .views import (HomePage, ActiveAstro, Spaceships, LifeSpace,
                    ViewNews, ViewBio, ViewVehicle, ViewLive,
                    Register, Login, LogOut)

urlpatterns = [

    # Register and Login
    path('register', Register, name='Register'),
    path('login', Login, name='Login'),
    path('logout', LogOut, name='Logout'),

    # Page with news
    path('', HomePage, name='Home'),
    path('news/<int:news_id>/', ViewNews, name='ViewNews'),

    #Page with astronauts
    path('astro/', ActiveAstro, name='Astro'),
    path('astro/<int:astro_id>/', ViewBio, name='ViewBio'),

    #Page with vehicle
    path('vehicle/', Spaceships, name='Vehicle'),
    path('vehicle/<int:vehicle_id>/', ViewVehicle, name='ViewVehicle'),

    # Page with live
    path('life/', LifeSpace, name='Life'),
    path('life/<int:article_id>/', ViewLive, name='ViewLive'),

    # Page with planets


    # path('space_object/<int:space_object_id>', UniverseList, name='Body'),
    # path('planet/<int:planet_id>/', ViewPlanet, name='ViewPlanet')
]
