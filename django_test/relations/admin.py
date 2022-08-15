from django.contrib import admin

from relations.models import Car, Car_owner, Colors

# Register your models here.

admin.site.register(Car)
admin.site.register(Car_owner)
admin.site.register(Colors)