from django.contrib import admin

from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    model = Service
    list_display = ['id', 'service', 'description', 'responsible', 'is_active']
    search_fields = ['service']
