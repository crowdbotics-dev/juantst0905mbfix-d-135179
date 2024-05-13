from django.contrib import admin
from .models import Liquid, Solid, Product

admin.site.register(Product)
admin.site.register(Solid)
admin.site.register(Liquid)

# Register your models here.
