from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group

admin.site.site_header = "Tipe Management Inventory Dashboard"

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','quantity','category')
    list_filter = ('category',)
# Register your models here.

admin.site.register(Product,ProductAdmin)
# admin.site.unregister(Group)
admin.site.register(Order)