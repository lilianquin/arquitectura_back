from django.contrib import admin

#Importando la tabla Productos
from .models import Productos

#Agregando al administrador
admin.site.register(Productos)
