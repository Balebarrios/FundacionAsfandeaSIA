from django.db import models
from personas_tea.models import Persona_tea
from usuarios_sis.models import Usuario_sis


class Citas(models.Model):
    LIBRE = '0'
    OCUPADA = '1'

    ESTADO_CHOICES = [(LIBRE, 'Libre'), (OCUPADA, 'Ocupada'), ]

    fecha_cita = models.DateField('Fecha Cita')
    hora_cita = models.TimeField('Hora cita')
    personatea = models.ForeignKey('personas_tea.Persona_tea', on_delete=models.CASCADE, verbose_name="Persona Tea")
    estado = models.CharField('Estado cita', max_length=1, choices=ESTADO_CHOICES, default=LIBRE)
    profesional = models.ForeignKey('usuarios_sis.Usuario_sis', on_delete=models.CASCADE, verbose_name="Profesional")


class Ficha_persona(models.Model):
    fecha_cre = models.DateField('Fecha Cita')
    hora_cre = models.TimeField('Hora cita')
    personatea = models.ForeignKey('personas_tea.Persona_tea', on_delete=models.CASCADE, verbose_name="Persona Tea")
    profesional = models.ForeignKey('usuarios_sis.Usuario_sis', on_delete=models.CASCADE, verbose_name="Profesional")
    comentarios = models.TextField('Comentarios')