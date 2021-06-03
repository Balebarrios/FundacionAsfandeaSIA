from django.contrib import admin
from ingresos.models import Donacion, Mensualidad, Actividad


# Register your models here.

class DonacionAdmin(admin.ModelAdmin):
    list_display = (
        "fecha", "hora", "glosa", "monto", "metodo_pago", "num_trans", "responsable", "tipo_dona", "donador")


admin.site.register(Donacion, DonacionAdmin)


class MensualidadAdmin(admin.ModelAdmin):
    list_display = (
        "fecha", "hora", "glosa", "monto", "metodo_pago", "num_trans", "responsable", "tipo_mens", "impositor")


admin.site.register(Mensualidad, MensualidadAdmin)


class ActividadAdmin(admin.ModelAdmin):
    list_display = (
        "fecha", "hora", "glosa", "monto", "metodo_pago", "num_trans", "responsable", "tipo_act", "impositor")


admin.site.register(Actividad, ActividadAdmin)