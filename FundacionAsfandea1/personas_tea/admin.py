from django.contrib import admin
from personas_tea.models import Persona_tea


# Register your models here.

class Persona_teaAdmin(admin.ModelAdmin):
    list_display = (
        "rut", "dni", "nombres", "apellidos", "fecha_nac", "nacionalidad", "direccion", "num_casa", "telefono", "email",
        "grado_tea")


admin.site.register(Persona_tea, Persona_teaAdmin)