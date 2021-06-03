from django.contrib import admin
from usuarios_sis.models import Usuario_sis


# Register your models here.


class Usuario_sisAdmin(admin.ModelAdmin):
    list_display = (
        "rut", "dni", "nombres", "apellidos", "fecha_nac", "nacionalidad", "direccion", "num_casa", "telefono", "email",
        "cargo")


admin.site.register(Usuario_sis, Usuario_sisAdmin)