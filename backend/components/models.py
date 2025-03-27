# components.models
from django.db import models

class ComponentCpuModel(models.Model):
    # Primary key
    component_cpu_id = models.BigAutoField(primary_key=True, verbose_name="CPU ID")

    # Store the combined component_cpu_name in the database for querying
    component_cpu_name = models.CharField(max_length=128, unique=True, db_index=True, verbose_name="CPU Name")

    # Fields for component_cpu_brand, component_cpu_series, and component_cpu_model
    component_cpu_brand = models.CharField(max_length=32, verbose_name="Brand", choices=[("AMD", "AMD"), ("Intel", "Intel")])
    component_cpu_series = models.CharField(max_length=32, verbose_name="Series")
    component_cpu_model = models.CharField(max_length=32, verbose_name="Model")

    component_cpu_socket = models.CharField(max_length=32, verbose_name="CPU Socket")
    component_cpu_clock_speed = models.DecimalField(max_digits=3, decimal_places=1, help_text="CPU clock speed in GHz")
    component_cpu_cores = models.PositiveIntegerField(verbose_name="Number of Cores")
    component_cpu_threads = models.PositiveIntegerField(verbose_name="Number of Threads")
    component_cpu_price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Cpu Price")
    component_cpu_image = models.ImageField(upload_to='components/cpu/', default='default_cpu.png', verbose_name="Cpu Image")

    class Meta:
        verbose_name = "CPU Component"
        verbose_name_plural = "CPU Components"
        # Ensure the combination of component_cpu_brand, component_cpu_series, and component_cpu_model is unique
        unique_together = [['component_cpu_brand', 'component_cpu_series', 'component_cpu_model']]

    def __str__(self):
        # Dynamically generate the CPU name
        return self.component_cpu_name


    def save(self, *args, **kwargs):
        # Before saving, generate the combined component_cpu_name
        if not self.component_cpu_name:  # Only generate component_cpu_name if it's not already set
            self.component_cpu_name = f"{self.component_cpu_brand} {self.component_cpu_series} {self.component_cpu_model}"
        super().save(*args, **kwargs)

class ComponentMemoryModel(models.Model):
    # Primary key
    component_memory_id = models.BigAutoField(primary_key=True, verbose_name="Memory ID")

    # Store the combined component_memory_name in the database for querying
    component_memory_name = models.CharField(max_length=128, unique=True, db_index=True, verbose_name="Memory Name")

    # Fields for component_memory_brand and component_memory_model
    component_memory_producer = models.CharField(max_length=128, verbose_name="Memory Producer")
    component_memory_model = models.CharField(max_length=128, verbose_name="Memory Model")

    component_memory_type = models.CharField(max_length=32, verbose_name="Memory Type", choices=[("DDR", "DDR"), ("DDR2", "DDR2"), ("DDR3", "DDR3"), ("DDR4", "DDR4")])
    component_memory_size = models.PositiveIntegerField(verbose_name="Memory Size")
    component_memory_clock_speed = models.PositiveIntegerField(verbose_name="Memory Clock Speed")
    component_memory_price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Memory Price")
    component_memory_image = models.ImageField(upload_to="components/memory", default="default_memory.png", verbose_name="Memory Image")

    class Meta:
        verbose_name = "Memory Component"
        verbose_name_plural = "Memory Components"
        # Ensure the combination of component_memory_producer and component_memory_model is unique
        unique_together = [['component_memory_producer', 'component_memory_model']]

    def __str__(self):
        # Dynamically generate the memory name
        return self.component_memory_name

    def save(self, *args, **kwargs):
        # Before saving, generate the combined component_memory_name
        if not self.component_memory_name:  # Only generate component_memory_name if it's not already set
            self.component_memory_name = f"{self.component_memory_producer} {self.component_memory_model}"
        super().save(*args, **kwargs)

class ComponentGpuModel(models.Model):
    # Primary key
    component_gpu_id = models.BigAutoField(primary_key=True, verbose_name="GPU ID")

    # Store the combined component_gpu_name in the database for querying
    component_gpu_name = models.CharField(max_length=128, unique=True, db_index=True, verbose_name="GPU Name")

    # Fields for component_gpu_brand and component_gpu_model
    component_gpu_brand = models.CharField(max_length=128, verbose_name="GPU Brand")
    component_gpu_model = models.CharField(max_length=128, verbose_name="GPU Model")
    component_gpu_series = models.CharField(max_length=128, verbose_name="GPU Series")

    component_gpu_vram = models.PositiveIntegerField(verbose_name="GPU Memory Size")
    component_gpu_boost_clock = models.PositiveIntegerField(verbose_name="GPU Boost Clock", help_text="CPU frequency in MHz")
    component_gpu_hdmi_port = models.PositiveIntegerField(verbose_name="GPU HDMI Port")
    component_gpu_power_consumption = models.PositiveIntegerField(verbose_name="GPU Power Consumption")
    component_gpu_price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="GPU Price")
    component_gpu_image = models.ImageField(upload_to="components/gpu/", default="default_gpu.png", verbose_name="GPU Image")

    class Meta:
        verbose_name = "GPU Component"
        verbose_name_plural = "GPU Components"
        # Ensure the combination of component_gpu_brand and component_gpu_model is unique
        unique_together = [['component_gpu_brand', 'component_gpu_model']]

    def __str__(self):
        # Dynamically generate the GPU name
        return self.component_gpu_name

    def save(self, *args, **kwargs):
        # Before saving, generate the combined component_gpu_name
        if not self.component_gpu_name:  # Only generate component_gpu_name if it's not already set
            self.component_gpu_name = f"{self.component_gpu_brand} {self.component_gpu_model} {self.component_gpu_series}"
        super().save(*args, **kwargs)

