from django.contrib import admin
from .models import French, Product, Solid, Spanish

admin.site.register(Product)
admin.site.register(Solid)
admin.site.register(French)
admin.site.register(Spanish)

# Register your models here.
