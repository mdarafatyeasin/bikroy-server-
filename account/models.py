from django.db import models
from .constants import GENDER, LOCATIONS, EDUCATION, ROLE
from django.contrib.auth.models import User

# Create your models here.
class basicInfo(models.Model):
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_picture     = models.ImageField(upload_to='profile_picture/', null=True)
    phone_number        = models.IntegerField()
    gender              = models.CharField(max_length=50, choices = GENDER, null=True)
    birth_date          = models.DateField(null=True)
    location            = models.CharField(max_length=50, choices=LOCATIONS, null=True)
    education_level     = models.CharField(max_length=50, choices=EDUCATION, null=True)
    current_job         = models.CharField(max_length=100, null=True)

class additionalInfo(models.Model):
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    about               = models.TextField(null=True)
    annual_income       = models.IntegerField(null=True)
    uv_name             = models.CharField(max_length=150, null=True)
    linkedin            = models.URLField(null=True)
    facebook            = models.URLField(null=True)

class userInfo(models.Model):
    user                = models.OneToOneField(User, on_delete=models.CASCADE)
    basicInfo           = models.ForeignKey(basicInfo, on_delete=models.CASCADE)
    additionalInfo      = models.ForeignKey(additionalInfo, on_delete=models.CASCADE)
    role                = models.CharField(max_length=10, choices=ROLE, null=True)