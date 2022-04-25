from django.db import models

# Create your models here.
class Product(models.Model):
    iProductId = models.AutoField(primary_key=True)
   

    vTitle = models.CharField(max_length=200)
    dPrice = models.DecimalField(decimal_places=2,max_digits=10,default=None)

    