from django.db import models


# Create your models here.


class Egreso(models.Model):
    fecha = models.DateField('Fecha egreso')
    hora = models.TimeField('Hora egreso')
    glosa = models.TextField('Glosa egreso')
    monto = models.IntegerField('Monto egreso')
    metodo_pago = models.CharField('Método de pago egreso', max_length=50)
    num_trans = models.IntegerField('Número de transacción egreso')
    responsable = models.CharField('Responsable', max_length=50)

    class Meta:
        abstract = True


class Gasto(Egreso):
    TIPO_1 = '01'
    TIPO_2 = '02'
    TIPO_3 = '03'

    TIPO_G_CHOICES = [
        (TIPO_1, 'Tipo 1'),
        (TIPO_2, 'Tipo 2'),
        (TIPO_3, 'Tipo 3'),
    ]

    tipo_gasto = models.CharField('Tipo de gasto', max_length=50, choices=TIPO_G_CHOICES, default=TIPO_1)
