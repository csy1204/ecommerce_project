from django.db import models
from accounts.models import User
# import time, datetime
from django.utils import timezone

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
    # Product.get_status_display
    status = models.PositiveSmallIntegerField(choices=STATUS, default=2)
    price = models.PositiveIntegerField() #default = 0 추가했었지만 placeholder 때문에 삭제
    image = models.ImageField(upload_to='img/', max_length=100, blank=True, null=True)
    seller = models.ForeignKey(User, default=1, on_delete=models.CASCADE, related_name="sell_list")
    wish = models.ManyToManyField(User, related_name='wish_list') # us
    cart = models.ManyToManyField(User, related_name='cart_list')
    end_time = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        """Unicode representation of Product."""
        return self.name

    def is_auction_end(self):
        now = timezone.localtime()
        return now > end_time



class AuctionHistory(models.Model):
    product = models.ForeignKey(Product, default=1, on_delete=models.CASCADE, related_name="auction_history")
    bidder = models.ForeignKey(User, default=1, on_delete=models.CASCADE, related_name="auction_list")
    price = models.PositiveIntegerField(default=0) #default = 0 추가
    
    class Meta:
        ordering = ['-price']




