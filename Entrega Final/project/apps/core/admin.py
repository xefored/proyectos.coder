from django.contrib import admin

from . import models

admin.site.register(models.Cliente)
admin.site.register(models.clientes_viajes)
admin.site.register(models.Destinos)
admin.site.register(models.Hoteles)
admin.site.register(models.Viaje)

