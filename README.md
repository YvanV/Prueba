# Prueba

## 1. Instalar el proyecto
#### Abrir sesion de terminal

git clone git@github.com:YvanV/Prueba.git

cd Prueba

python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

## 2. Poblar datos
#### Demora 23 minutos aproximadamente

python genera_datos.py

## 3. Ejecutar proyecto

python manage.py runserver

## 4. Acceder a la vista principal

http://localhost:8000/






