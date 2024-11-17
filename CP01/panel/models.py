# models.py
from django.db import models

class Mower(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=[
        ('on', 'Encendido'),
        ('off', 'Apagado'),
        ('paused', 'En Pausa'),
        ('operating', 'Operando')
    ])
    battery_level = models.DecimalField(max_digits=5, decimal_places=2)
    last_update = models.DateTimeField(auto_now=True)

class Command(models.Model):
    mower = models.ForeignKey(Mower, related_name='commands', on_delete=models.CASCADE)
    command_type = models.CharField(max_length=50, choices=[
        ('start', 'Encender'),
        ('stop', 'Apagar'),
        ('pause', 'Pausar'),
        ('continue', 'Continuar')
    ])
    timestamp = models.DateTimeField(auto_now_add=True)

class SensorData(models.Model):
    mower = models.ForeignKey(Mower, related_name='sensor_data', on_delete=models.CASCADE)
    obstacle_detected = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Route(models.Model):
    mower = models.ForeignKey(Mower, related_name='route', on_delete=models.CASCADE)
    position_x = models.DecimalField(max_digits=10, decimal_places=2)
    position_y = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
