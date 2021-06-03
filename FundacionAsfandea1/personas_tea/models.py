from django.db import models


# Create your models here.
class Persona(models.Model):
    rut = models.CharField('Rut', max_length=10, blank=False, null=False)
    dni = models.CharField('Dni', max_length=10, blank=False, null=False)
    nombres = models.CharField('Nombres', max_length=40, blank=False, null=False)
    apellidos = models.CharField('Apellidos', max_length=40, blank=False, null=False)
    fecha_nac = models.DateField('Fecha de nacimiento')
    nacionalidad = models.CharField('Nacionalidad', max_length=30, blank=False, null=False)
    direccion = models.CharField('Dirección', max_length=30, blank=False, null=False)
    num_casa = models.CharField('Número de casa', max_length=6, blank=False, null=False)
    telefono = models.CharField('Teléfono', max_length=9, blank=False, null=False)
    email = models.EmailField('Correo Electrónico', blank=False, null=False)

    class Meta:
        abstract = True


class Persona_tea(Persona):
    GRADO_1 = '01'
    GRADO_2 = '02'
    GRADO_3 = '03'
    GRADO_4 = '04'

    GRADOS_CHOICES = [
        (GRADO_1, 'Grado 1'),
        (GRADO_2, 'Grado 2'),
        (GRADO_3, 'Grado 3'),
        (GRADO_4, 'Grado 4'),

    ]

    grado_tea = models.CharField('Grado de tea', max_length=20, choices=GRADOS_CHOICES, default=GRADO_1)