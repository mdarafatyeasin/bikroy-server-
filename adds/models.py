from django.db import models
from .constants import CONDITION, AUTHENTICITY, LOCATIONS
from django.contrib.auth.models import User

# Create your models here.
class addModel(models.Model):
    author          = models.ForeignKey(User, on_delete=models.CASCADE)
    condition       = models.CharField(max_length=15, choices=CONDITION)
    authenticity    = models.CharField(max_length=15, choices=AUTHENTICITY)
    brand_name      = models.CharField(max_length=100)
    model           = models.CharField(max_length=100)
    description     = models.TextField()
    price           = models.IntegerField()
    negotiable      = models.BooleanField()
    picture         = models.URLField(null=True)
    contact         = models.CharField(max_length=15)
    location        = models.CharField(max_length=50, choices=LOCATIONS, null=True, blank=True)