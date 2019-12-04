from django.db import models

class Product(models.Model):
    """Model definition for Product."""

    # TODO: Define fields here
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    trading_place = models.TextField()
    status = models.CharField(max_length=30)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='img/', max_length=100)
    
    def __str__(self):
        """Unicode representation of Product."""
        return self.name





