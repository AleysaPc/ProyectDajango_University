from django.contrib import admin
#Importamos el modelo curso
from .models import Curso

# Register your models here.
#Panel de administracion
admin.site.register(Curso)
