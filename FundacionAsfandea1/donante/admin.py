from django.contrib import admin
from donante.models import Donante


# Register your models here.

class DonanteAdmin(admin.ModelAdmin):
    list_display = (
        "rut", "dni", "nombres", "apellidos", "fecha_nac", "nacionalidad", "direccion", "num_casa", "telefono", "email",
        "tipo_donante")


admin.site.register(Donante, DonanteAdmin)