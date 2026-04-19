#!/usr/bin/env bash
# Salir si hay un error
set -o errexit

# Instalar las librerías necesarias (Django, etc.)
pip install -r requirements.txt

# Recolectar archivos de diseño (CSS, imágenes)
python manage.py collectstatic --no-input

# Actualizar la base de datos en el servidor de Render
python manage.py migrate