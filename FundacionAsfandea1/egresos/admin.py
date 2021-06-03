from django.contrib import admin
from egresos.models import Gasto


# Register your models here.

class GastoAdmin(admin.ModelAdmin):
    list_display = (
        "fecha", "hora", "glosa", "monto", "metodo_pago", "num_trans", "responsable", "tipo_gasto")


admin.site.register(Gasto, GastoAdmin)