from django.contrib import admin
from .models import course,customerorder,inventory,tempcart,suppliments
# Register your models here.

admin.site.register(customerorder)
admin.site.register(course)
admin.site.register(inventory)
admin.site.register(tempcart)
admin.site.register(suppliments)