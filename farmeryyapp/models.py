
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.



class Info(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    phno = models.CharField(max_length=12)
    refphno= models.CharField(max_length=12)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    objects=models.Manager()




class Product(models.Model):
	
    productname = models.CharField(max_length=30)        
    category= models.CharField(max_length=20, blank=True)
    desc= models.CharField(max_length=30)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField()
    img= models.ImageField(null=True, blank=True)
    discountdesc = models.CharField(max_length=50,blank=True)
    oldprice = models.CharField(max_length=10,blank=True)
    newdiscount = models.CharField(max_length=10,blank=True)
    objects=models.Manager()

class Category1(models.Model):
    id=models.AutoField(primary_key=True)
    cattype = models.CharField(max_length=20)
    objects=models.Manager()


class ProductType(models.Model):
    id=models.AutoField(primary_key=True)
    protype = models.CharField(max_length=30)
   
class Product2(models.Model):
    id=models.AutoField(primary_key=True)
    category1_id=models.ForeignKey(Category1,on_delete=models.CASCADE)
    proname=models.CharField(max_length=30) 
    pric=models.IntegerField()
    quant=models.IntegerField()
    farmer_name=models.CharField(max_length=30,blank=True) 
    orchard= models.CharField(max_length=40,blank=True)
    producttype_id=models.ForeignKey(ProductType,on_delete=models.DO_NOTHING)
    expted_delivery=models.DateField()
    pre_delivery=models.DateField()
    proimg= models.ImageField(null=True, blank=True)

class Team(models.Model):
    id=models.AutoField(primary_key=True)
    tname= models.CharField(max_length=20)
    timg=models.ImageField(null=True, blank=True)
    tdesc=models.CharField(max_length=100)
    


class Rating(models.Model):
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars= models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    review=models.CharField(max_length=255)
    class Meta:
        unique_together=(('user','product_id'),)  #if same user give rating to one movie 2 times it will be rejected
        index_together=(('user','product_id'),)

