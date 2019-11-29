from django.db import models

class Product(models.Model):
    """Model definition for Product."""

    # TODO: Define fields here
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)



    def __str__(self):
        """Unicode representation of Product."""
        pass

