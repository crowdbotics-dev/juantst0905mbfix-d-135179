from django.contrib import admin
from .models import Mdns, French, Solid, Product

admin.site.register(Product)
admin.site.register(Solid)
admin.site.register(French)
admin.site.register(Mdns)

# Register your models here.
