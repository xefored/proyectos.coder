
from django.urls import path

from . import views



urlpatterns = [
    path("", views.index, name="index" ),
    path("Hoteles/list", views.Hoteles_list, name="Hoteles_list" ),
    path("Hoteles/form", views.Hoteles_form, name="Hoteles_form" ),
    path("Destinos/list", views.Destinos_list, name="Destinos_list" ),
    path("Destinos/form", views.Destinos_form, name="Destinos_form" ),
    path("core/login", views.CustomLoginView.as_view, name="Login"),
]
