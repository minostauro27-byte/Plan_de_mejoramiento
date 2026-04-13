from django.db import models
from django.conf import settings

class Ticket(models.Model):
    ESTADOS = (
        ('pendiente', 'Pendiente'),
        ('en_revision', 'En Revisión'),
        ('resuelto', 'Resuelto'),
    )

    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    numero_equipo = models.CharField(max_length=50)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_resolucion = models.DateTimeField(null=True, blank=True)