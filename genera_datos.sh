#!/bin/bash

python ./genera_datos_parte1.py

sqlite3 db.sqlite3 < genera_datos_parte2.sql

rm interactions.csv
