from django.contrib import admin

# Register your models here.
from .models import Aircraft

# Register your models here.
class AircraftAdmin(admin.ModelAdmin): # Para que se puedan ver los campos created y updated
    readonly_fields = ('created', 'updated')

admin.site.register(Aircraft, AircraftAdmin)