from django.db import models

class ComponentCpuModel(models.Model):
    # Primary key
    component_cpu_id = models.BigAutoField(primary_key=True, verbose_name="CPU ID")

    # Fields for component_cpu_brand, component_cpu_series, and component_cpu_model
    component_cpu_brand = models.CharField(max_length=32, verbose_name="Brand", choices=[("AMD", "AMD"), ("Intel", "Intel")])
    component_cpu_series = models.CharField(max_length=32, verbose_name="Series")
    component_cpu_model = models.CharField(max_length=32, verbose_name="Model")

    # Store the combined component_cpu_name in the database for querying
    component_cpu_name = models.CharField(max_length=128, unique=True, db_index=True, verbose_name="CPU Name")
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