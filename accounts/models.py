from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
CHOISES=(
    ('Buy','Buyer'),
    ('Sell','Seller')
)

class User(AbstractUser):
    username = models.CharField(max_length=45, blank=False, primary_key=True)
    name = models.CharField(max_length=45, blank = False)
    pw = models.CharField(max_length=45, default=True)
    id = models.CharField(max_length=45, default=True)
    classification = models.CharField(max_length=10, blank=False,choices=CHOISES)