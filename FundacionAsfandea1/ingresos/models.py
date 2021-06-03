from django.db import models
from donante.models import Donante
from apoderados.models import Apoderado


# Create your models here.

class Ingreso(models.Model):
    fecha = models.DateField('Fecha ingreso')
    hora = models.TimeField('Hora ingreso')
    glosa = models.TextField('Glosa ingreso')
    monto = models.IntegerField('Monto ingreso')
    metodo_pago = models.CharField('Método de pago ingreso', max_length=50)
    num_trans = models.IntegerField('Número de transacción ingreso')
    responsable = models.CharField('Responsable', max_length=50)

    class Meta:
        abstract = True


class Donacion(Ingreso):
    TIPO_1 = '01'
    TIPO_2 = '02'
    TIPO_3 = '03'

    TIPO_D_CHOICES = [
        (TIPO_1, 'Tipo 1'),
        (TIPO_2, 'Tipo 2'),
        (TIPO_3, 'Tipo 3'),
    ]

    tipo_dona = models.CharField('Tipo de donación', max_length=50, choices=TIPO_D_CHOICES, default=TIPO_1)
    donador = models.ForeignKey('donante.Donante', on_delete=models.CASCADE, verbose_name="Donador")


class Mensualidad(Ingreso):
    TIPO_1 = '01'
    TIPO_2 = '02'
    TIPO_3 = '03'

    TIPO_M_CHOICES = [
        (TIPO_1, 'Tipo 1'),
        (TIPO_2, 'Tipo 2'),
        (TIPO_3, 'Tipo 3'),
    ]

    tipo_mens = models.CharField('Tipo de mensualidad', max_length=50, choices=TIPO_M_CHOICES, default=TIPO_1)
    impositor = models.ForeignKey('apoderados.Apoderado', on_delete=models.CASCADE, verbose_name="Persona que paga")


class Actividad(Ingreso):
    TIPO_1 = '01'
    TIPO_2 = '02'
    TIPO_3 = '03'

    TIPO_A_CHOICES = [
        (TIPO_1, 'Tipo 1'),
        (TIPO_2, 'Tipo 2'),
        (TIPO_3, 'Tipo 3'),
    ]

    tipo_act = models.CharField('Tipo de actividad', max_length=50, choices=TIPO_A_CHOICES, default=TIPO_1)
    impositor = models.ForeignKey('apoderados.Apoderado', on_delete=models.CASCADE, verbose_name="Persona que paga")
