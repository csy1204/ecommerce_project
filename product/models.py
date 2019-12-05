from django.db import models
from accounts.models import User

class Product(models.Model):
    """Model definition for Product."""
    STATUS = (
      (1, 'auction'),
      (2, 'purchased in progress'),
      (3, 'purchased completed'),
   )

    # TODO: Define fields here
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    trading_place = models.TextField()
    status = models.PositiveSmallIntegerField(choices=STATUS, default=2)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='img/', max_length=100, blank=True, null=True)
    wish = models.ManyToManyField(User, related_name='wish_list')
    cart = models.ManyToManyField(User, related_name='cart_list')

    def __str__(self):
        """Unicode representation of Product."""
        return self.name


class AuctionHistory(models.Model):
    pass



