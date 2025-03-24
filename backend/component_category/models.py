from django.db import models

class ComponentCategoryModel(models.Model):
    """
    Model representing a category for components.

    This model stores information about a category, including its name, title, subtitle,
    and description. Each category has a unique name and is indexed for faster queries.
    """

    # Primary key for the category
    component_category_id = models.BigAutoField(primary_key=True)

    # Name of the category (unique and indexed for faster lookups)
    component_category_name = models.CharField(max_length=64, unique=True, db_index=True)

    # Title of the category
    component_category_title = models.CharField(max_length=64)

    # Subtitle of the category (can be longer than the title)
    component_category_sub_title = models.TextField()

    # Description of the category (can be a detailed explanation)
    component_category_description = models.TextField()

    def __str__(self) -> str:
        """
        Returns a string representation of the category.

        This method is used to display the category's name in the Django admin interface
        and other places where a string representation is needed.

        Returns:
            str: The name of the category.
        """
        return self.component_category_name

