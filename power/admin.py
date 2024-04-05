from django.contrib import admin

# Register your models here.
from power import models

admin.site.register(models.Product)
admin.site.register(models.ProductDetail)
admin.site.register(models.GlobalParam)
admin.site.register(models.TestUnit)
admin.site.register(models.UnitParam)