from django.contrib import admin

from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ['nume', 'prenume', 'adresa', 'oras', 'cod_postal']


admin.site.register(Order, OrderAdmin)
