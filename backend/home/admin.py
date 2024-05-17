from django.contrib import admin
from .models import French, Solid, Product

admin.site.register(Product)
admin.site.register(Solid)
admin.site.register(French)

# Register your models here.
