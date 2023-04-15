from django.contrib import admin
from .models import customerorder,inventory,tempcart
# Register your models here.

admin.site.register(customerorder)
admin.site.register(inventory)
admin.site.register(tempcart)
