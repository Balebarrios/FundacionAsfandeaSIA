from django.contrib import admin
from apoderados.models import Apoderado


class ApoderadoAdmin(admin.ModelAdmin):
    list_display = (
        "rut", "dni", "nombres", "apellidos", "fecha_nac", "nacionalidad", "direccion", "num_casa", "telefono", "email",
        "relacion", "personatea")


admin.site.register(Apoderado, ApoderadoAdmin)