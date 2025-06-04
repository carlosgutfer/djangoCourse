from django.db import models

# Create your models here.
class Aircraft(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=200)
    manufacturer = models.CharField(verbose_name='Fabricante', max_length=100)
    model = models.CharField(verbose_name='Modelo', max_length=100)
    serial_number = models.CharField(verbose_name='Número de serie', max_length=100, unique=True)
    registration_number = models.CharField(verbose_name='Matrícula', max_length=50, unique=True)
    aircraft_type = models.CharField(verbose_name='Tipo de aeronave', max_length=50)  # e.g., Jet, Helicóptero, etc.
    seating_capacity = models.IntegerField(verbose_name='Capacidad de pasajeros')
    max_takeoff_weight = models.DecimalField(verbose_name='Peso máximo de despegue (kg)', max_digits=10, decimal_places=2)
    empty_weight = models.DecimalField(verbose_name='Peso en vacío (kg)', max_digits=10, decimal_places=2)
    wingspan = models.DecimalField(verbose_name='Envergadura (m)', max_digits=6, decimal_places=2)
    length = models.DecimalField(verbose_name='Longitud (m)', max_digits=6, decimal_places=2)
    height = models.DecimalField(verbose_name='Altura (m)', max_digits=6, decimal_places=2)
    max_speed = models.IntegerField(verbose_name='Velocidad máxima (km/h)')
    cruise_speed = models.IntegerField(verbose_name='Velocidad de crucero (km/h)')
    range_km = models.IntegerField(verbose_name='Alcance máximo (km)')
    fuel_capacity = models.DecimalField(verbose_name='Capacidad de combustible (litros)', max_digits=10, decimal_places=2)
    engine_type = models.CharField(verbose_name='Tipo de motor', max_length=100)
    number_of_engines = models.IntegerField(verbose_name='Número de motores')
    year_of_manufacture = models.PositiveIntegerField(verbose_name='Año de fabricación')
    in_service = models.BooleanField(verbose_name='En servicio', default=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Avión"
        verbose_name_plural = "Aviones"
        ordering = ['model', 'manufacturer']

    def __str__(self):
        return self.name