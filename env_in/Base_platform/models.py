from django.db import models
from django.contrib.auth.models import AbstractUser, User
# Create your models here.

class User_Details(AbstractUser):
    Name        = models.CharField(max_length=255,blank=True)
    Mobile      = models.CharField(max_length=255,blank=True)
    AccountType = models.CharField(max_length=255,default="Basic")
    Leaf        = models.CharField(max_length=255,default="0")
    Bio         = models.TextField(default="A Eco In user")
    Job         = models.CharField(max_length=255,default="Not Specified")
    Img         = models.ImageField(blank=True)
    REQUIRED_FIELDS: list()
    def __str__(self):
        return self.username
    class Meta:
          verbose_name = 'User_Details'
          verbose_name_plural=verbose_name
