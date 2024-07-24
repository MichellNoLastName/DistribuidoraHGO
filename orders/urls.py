from django.urls import path
from . import views

app_name = 'orders'
urlpatterns = [
    path('add/',views.add_order,name='add_order'),
    path('add/load_towns/',views.load_towns,name='load_towns'),
    path('add/load_streets/',views.load_streets,name='load_streets'),
    path('add/load_location/',views.load_location,name='load_location'),
]
