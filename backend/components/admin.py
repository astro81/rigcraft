from django.contrib import admin
from .models import ComponentCpuModel, ComponentMemoryModel, ComponentGpuModel

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

@admin.register(ComponentMemoryModel)
class ComponentMemoryModelAdmin(admin.ModelAdmin):
    list_display = ('component_memory_name', 'component_memory_producer', 'component_memory_model')
    readonly_fields = ('component_memory_name',)  # Make component_memory_name read-only
    exclude = ('component_memory_name',)  # Exclude component_memory_name from the form

    search_fields = ('component_memory_name', 'component_memory_producer', 'component_memory_type') # Enables a search bar to filter instances based on specific fields.
    list_filter = ('component_memory_producer', 'component_memory_type', 'component_memory_size')  # Provides a filter to allow users to view instances based on specific fields.
    # Groups fields into sections in the add/edit form
    fieldsets = (
        ('Basic Information', {
            'fields': ('component_memory_producer', 'component_memory_model', 'component_memory_type')
        }),
        ('Advanced Information', {
            'fields': ('component_memory_size', 'component_memory_clock_speed', 'component_memory_price', 'component_memory_image')
        }),
    )

@admin.register(ComponentGpuModel)
class ComponentGpuModelAdmin(admin.ModelAdmin):
    list_display = ('component_gpu_name', 'component_gpu_brand', 'component_gpu_series', 'component_gpu_model')
    readonly_fields = ('component_gpu_name',)  # Make component_gpu_name read-only
    exclude = ('component_gpu_name',)  # Exclude component_gpu_name from the form

    search_fields = ('component_gpu_name', 'component_gpu_brand', 'component_gpu_model', 'component_gpu_series') # Enables a search bar to filter instances based on specific fields.
    list_filter = ('component_gpu_brand', 'component_gpu_series', 'component_gpu_vram')  # Provides a filter to allow users to view instances based on specific fields.
    # Groups fields into sections in the add/edit form
    fieldsets = (
        ('Basic Information', {
            'fields': ('component_gpu_brand', 'component_gpu_model', 'component_gpu_series')
        }),
        ('Advanced Information', {
            'fields': ('component_gpu_vram', 'component_gpu_boost_clock', 'component_gpu_hdmi_port', 'component_gpu_power_consumption', 'component_gpu_price', 'component_gpu_image')
        }),
    )