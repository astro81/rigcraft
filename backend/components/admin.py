from django.contrib import admin
from .models import ComponentCpuModel

@admin.register(ComponentCpuModel)
class ComponentCpuModelAdmin(admin.ModelAdmin):
    list_display = ('component_cpu_name', 'component_cpu_brand', 'component_cpu_series', 'component_cpu_model')
    readonly_fields = ('component_cpu_name',)  # Make component_cpu_name read-only
    exclude = ('component_cpu_name',)  # Exclude component_cpu_name from the form

    search_fields = ('component_cpu_name', 'component_cpu_brand') # Enables a search bar to filter instances based on specific fields.
    list_filter = ('component_cpu_brand', 'component_cpu_series')  # Provides a filter to allow users to view instances based on specific fields.
    # Groups fields into sections in the add/edit form
    fieldsets = (
        ('Basic Information', {
            'fields': ('component_cpu_brand', 'component_cpu_series', 'component_cpu_model')
        }),
        ('Advanced Information', {
            'fields': ('component_cpu_socket', 'component_cpu_clock_speed', 'component_cpu_cores', 'component_cpu_threads', 'component_cpu_price', 'component_cpu_image')
        }),
    )