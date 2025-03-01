from django.db import models

# Create your models here.
class ComponentCategoryModel(models.Model):
    component_category_id = models.BigAutoField(primary_key=True)
    component_category_name = models.CharField(max_length=64, unique=True, db_index=True)
    component_category_title = models.CharField(max_length=64)
    component_category_sub_title = models.TextField()
    component_category_description = models.TextField()

    def __str__(self):
        return self.component_category_name