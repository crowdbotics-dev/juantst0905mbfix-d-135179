from django.contrib import admin
from .models import Rdsc, French, Solid, Product

admin.site.register(Product)
admin.site.register(Solid)
admin.site.register(French)
admin.site.register(Rdsc)

# Register your models here.
