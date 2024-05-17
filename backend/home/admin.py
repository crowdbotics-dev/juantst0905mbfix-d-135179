from django.contrib import admin
from .models import French, Product, Rdsc, Solid

admin.site.register(Product)
admin.site.register(Solid)
admin.site.register(French)
admin.site.register(Rdsc)

# Register your models here.
