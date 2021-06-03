from django.contrib import admin
from citas.models import Citas, Ficha_persona


class CitasAdmin(admin.ModelAdmin):
    list_display = ("fecha_cita", "hora_cita", "personatea", "estado", "profesional")


admin.site.register(Citas, CitasAdmin)


class Ficha_personaAdmin(admin.ModelAdmin):
    list_display = ("fecha_cre", "hora_cre", "personatea", "profesional", "comentarios")


admin.site.register(Ficha_persona, Ficha_personaAdmin)