import datetime
from django.shortcuts import render
import pytz

from Aplicacion.forms import BuscaCustomersForm
from Aplicacion.models import Customers, Interactions

import logging

# Create your views here.

from django.db.models import F

def customersView(request):

    def get_campo(customer):
        valor = customer.get(ordenar)
        return valor

    customers = Customers.objects.all()
    form = BuscaCustomersForm(request.GET)
    nombreBuscado = request.GET.get('nombre')
    cumpleanhosBuscado = request.GET.get('criterio_cumpleanhos')
    ordenar = request.GET.get('criterio_ordenar')

    if nombreBuscado is not None and nombreBuscado != "":
        customers = customers.filter(nombre__icontains=nombreBuscado)
    if cumpleanhosBuscado is not None and cumpleanhosBuscado != "":
        hoy = datetime.date.today()
        if cumpleanhosBuscado == "hoy":
            customers = [obj for obj in customers if obj.cumpleanhos_actual() == hoy]
        elif cumpleanhosBuscado == "esta_semana":
            customers = [obj for obj in customers if obj.cumpleanhos_actual().isocalendar()[0:2] == hoy.isocalendar()[0:2]]
        elif cumpleanhosBuscado == "este_mes":
            customers = [obj for obj in customers if obj.cumpleanhos_actual().month == hoy.month]
        else:
            pass

    list_customers = []
    for c in customers:
        customer = {"nombre": c.nombre, "company": c.company.nombre, "fecha_nacimiento": c.fecha_nacimiento, "cumpleanhos_actual": c.cumpleanhos_actual()}
        interactions = Interactions.objects.filter(customer = c).order_by("-fecha_interaccion")        
        ultimaInteracion = interactions.first() if interactions else None
        customer["tipo"] = ultimaInteracion.tipo if ultimaInteracion else None
        customer["fecha_interaccion"] = ultimaInteracion.fecha_interaccion if ultimaInteracion else None
        customer["calculated_value"] = c.cumpleanhos_actual()
        list_customers.append(customer)

    if ordenar:
        if ordenar == "fecha_interaccion":
            list_customers.sort(key=get_campo, reverse=True)
        else:
            list_customers.sort(key=get_campo)

    contexto = {
        "form": form,
        "customers": list_customers}
    return render(request, 'Aplicacion/customers.html', contexto)    
