from django.db import models
from django.utils import timezone
from Base_platform.models import User_Details

class Labels(models.Model):
    Name    =   models.CharField(max_length=50,unique=True)
    def __str__(self):
        return self.Name
    class Meta:
        verbose_name = "Lables"
        verbose_name_plural=verbose_name

class Product(models.Model):
    Name    =   models.CharField(max_length=150)
    Desc    =   models.TextField(default="")
    Img     =   models.ImageField()
    Company =   models.CharField(max_length=150)
    Stock   =   models.CharField(max_length=10)
    Created =   models.DateTimeField(timezone.now)
    Price   =   models.CharField(max_length=10)
    Type    =   models.CharField(max_length=10,default="New")
    Leafs   =   models.CharField(max_length=10,default="0")
    def __str__(self):
        return self.Name
    class Meta:
        verbose_name = "Product"
        verbose_name_plural=verbose_name

class Cart(models.Model):
    User    =   models.ForeignKey(User_Details,on_delete=models.DO_NOTHING)
    Prod_Id =   models.ManyToManyField(Product)
    Qty     =   models.CharField(max_length=10)
    class Meta:
        verbose_name = "Cart"
        verbose_name_plural=verbose_name



