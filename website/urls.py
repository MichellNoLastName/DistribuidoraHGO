from django.urls import path
from . import views

app_name="website"

urlpatterns = [
    path("",views.index,name="index"),
    path("index/",views.index,name="index"),
    path("about_us/",views.aboutus,name="aboutus"),
]
