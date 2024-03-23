from django.contrib import admin
from .models import Animal, Adoption


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'available', 'created', 'updated']
    list_filter = ['available']
    prepopulated_fields = {'slug': ('name',)}


class AdoptionAdmin(admin.ModelAdmin):
    list_display = ['user', 'nume', 'prenume', 'adresa', 'oras', 'telefon', 'email', 'adapost']


admin.site.register(Adoption, AdoptionAdmin)
