import csv
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Prueba.settings")
import django
django.setup()

from Aplicacion.models import Users, Companies, Customers, Interactions
import random

from faker import Faker
fake_es = Faker('es_ES')

maxUsers = 3
for _ in range(maxUsers):
    user = Users(nombre = fake_es.name(),
        email = fake_es.email(),
        contrasenha = "clave123",
        es_administrador = False)
    user.save()
print("Cantidad de Users:", Users.objects.all().count())

maxCompanies = 50
for _ in range(maxCompanies):
    company = Companies(nombre = fake_es.company())
    company.save()
print("Cantidad de Companies:", Companies.objects.all().count())

maxCustomers = 1000
for _ in range(maxCustomers):
    customer = Customers(
        nombre = fake_es.name(),
        fecha_nacimiento = fake_es.date_of_birth(),
        company = Companies.objects.get(id=random.choice([c.id for c in Companies.objects.all()])),
        user = Users.objects.get(id=random.choice([u.id for u in Users.objects.all()]))
        )
    customer.save()
print("Cantidad de customers:", Customers.objects.all().count())


from django.utils import timezone
import pytz

maxInteractions = 500
customersTotal = Customers.objects.all().count()
customersProcessed = 0
list_interactions =[]
for customer in Customers.objects.all():
    customersProcessed = customersProcessed + 1
    for _ in range(maxInteractions):
        """
        interaction = Interactions(
            customer = customer,
            tipo = random.choice(["Call", "Email", "SMS", "Facebook"]),
            fecha_interaccion = fake_es.past_datetime(start_date='-5y', tzinfo=pytz.timezone('America/Lima'))
        )
        interaction.save()
        """
        list_interactions.append([
            random.choice(["Call", "Email", "SMS", "Facebook"]), 
            fake_es.past_datetime(start_date='-5y', tzinfo=pytz.timezone('America/Lima')),
            customer.id ])
    print(".", end="", flush=True)
    if customersProcessed % 100 == 0:
        print(f"{customersProcessed}/{customersTotal}")

with open('interactions.csv', 'w', newline='') as myfile:
    # wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr = csv.writer(myfile)
    wr.writerows(list_interactions)

# print("Cantidad de interacciones:", Interactions.objects.all().count())

    