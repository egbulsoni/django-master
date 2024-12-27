from django.contrib import admin
from cars.models import *

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'make', 'factory_year', 'model_year', 'price')
    search_fields = ('model',)

class MakeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Car, CarAdmin)
admin.site.register(Make, MakeAdmin)