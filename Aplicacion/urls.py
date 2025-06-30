

from django.urls import path
from . import views

from Aplicacion.views import customersView

urlpatterns = [
    path("customers/", customersView, name = "customers"), #
    path("", customersView, name = "home"), #
    
]

