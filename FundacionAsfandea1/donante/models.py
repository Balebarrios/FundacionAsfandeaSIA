from django.db import models
from personas_tea.models import Persona


# Create your models here.

class Donante(Persona):
    TIPO_1 = '01'
    TIPO_2 = '02'

    DONA_CHOICES = [
        (TIPO_1, 'Relación 1'),
        (TIPO_2, 'Relación 2'),
    ]

    tipo_donante = models.CharField('Tipo de donante', max_length=20, choices=DONA_CHOICES, default=TIPO_1)
