from django.db import models


# Create your models here.

class Usuario_sis(models.Model):
    CARGO_1 = '01'
    CARGO_2 = '02'
    CARGO_3 = '03'
    CARGO_4 = '04'

    CARGOS_CHOICES = [
        (CARGO_1, 'Cargo A'),
        (CARGO_2, 'Cargo B'),
        (CARGO_3, 'Cargo C'),
        (CARGO_4, 'Cargo D'),

    ]

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
    cargo = models.CharField('Cargo',max_length=20, choices=CARGOS_CHOICES, default=CARGO_1)