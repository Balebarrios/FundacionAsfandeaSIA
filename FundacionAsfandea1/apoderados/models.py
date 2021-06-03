from django.db import models
from personas_tea.models import Persona, Persona_tea


class Apoderado(Persona):
    RELACION_1 = '01'
    RELACION_2 = '02'
    RELACION_3 = '03'
    RELACION_4 = '04'

    RELATION_CHOICES = [
        (RELACION_1, 'Relación 1'),
        (RELACION_2, 'Relación 2'),
        (RELACION_3, 'Relación 3'),
        (RELACION_4, 'Relación 4'),

    ]

    relacion = models.CharField('Relación con paciente', max_length=20, choices=RELATION_CHOICES, default=RELACION_1)
    personatea = models.ForeignKey('personas_tea.Persona_tea', on_delete=models.CASCADE)