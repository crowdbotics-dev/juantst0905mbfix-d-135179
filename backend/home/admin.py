from django.contrib import admin
from .models import ACvs, French, Solid, Product

admin.site.register(Product)
admin.site.register(Solid)
admin.site.register(French)
admin.site.register(ACvs)

# Register your models here.
