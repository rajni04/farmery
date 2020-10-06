
from django.db import models

from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.core.validators import RegexValidator



class CustomUser(AbstractUser):
    user_type_data=((1,"ADMIN"),(2,"CUSTOMER"))
    user_type=models.CharField(default=1,choices=user_type_data,max_length=10)
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

    first_name=models.CharField(max_length=10, validators=[alphanumeric])
    last_name=models.CharField(max_length=10)
    email=models.EmailField(max_length=20)
   

class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()


class Customer(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    address=models.TextField(max_length=50)
   
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Info(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    phno = models.CharField(max_length=12)
    refphno= models.CharField(max_length=12)
    
    objects=models.Manager()




class Product(models.Model):
    id=models.AutoField(primary_key=True)
    productname = models.CharField(max_length=30,null=False)        
    categoryy= models.CharField(max_length=20, blank=True,default=1)
    desc= models.CharField(max_length=30)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField()
    img= models.ImageField(null=True, blank=True)
    discountdesc = models.CharField(max_length=50,blank=True)
    oldprice = models.CharField(max_length=10,blank=True)
    newdiscount = models.CharField(max_length=10,blank=True)
    objects=models.Manager()

    def __str__(self):
        return self.productname

class Category1(models.Model):
    id=models.AutoField(primary_key=True)
    cattype = models.CharField(max_length=20)
    objects=models.Manager()

class Subcategory(models.Model):
    id=models.AutoField(primary_key=True)
    subcategory_name = models.CharField(max_length=30)
    category_id=models.ForeignKey(Category1,on_delete=models.CASCADE)
    

class ProductType(models.Model):
    id=models.AutoField(primary_key=True)
    protype = models.CharField(max_length=30)
    

class Product2(models.Model):
    id=models.AutoField(primary_key=True)
    category_id=models.ForeignKey(Category1,on_delete=models.CASCADE)
    subcategory_id=models.ForeignKey(Subcategory,on_delete=models.CASCADE,blank=True,null=True)
    proname=models.CharField(max_length=30) 
    pric=models.IntegerField()
    quant=models.IntegerField()
    farmer_name=models.CharField(max_length=30,blank=True) 
    orchard= models.CharField(max_length=40,blank=True)
    expted_delivery=models.DateField()
    pre_delivery=models.DateField()
    img= models.ImageField(null=True, blank=True)

class Team(models.Model):
    id=models.AutoField(primary_key=True)
    tabt= models.CharField(max_length=100)
    tname= models.CharField(max_length=20)
    timg=models.ImageField(null=True, blank=True)
    tdesc=models.CharField(max_length=255)
    


class Rating(models.Model):
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)

    stars= models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    review=models.CharField(max_length=255)
    

class Productview(models.Model):
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    trialdays=models.CharField(max_length=255)

class Work(models.Model):
    headng=models.CharField(max_length=30)
    headng2=models.CharField(max_length=30)
    workdesc=models.CharField(max_length=255)
    workdesc2=models.CharField(max_length=255)
    wimg=models.ImageField(null=True, blank=True)
    wimg2=models.ImageField(null=True, blank=True)


class Circl(models.Model):
    cheading=models.CharField(max_length=50)  
    cdesc=models.CharField(max_length=500)
    che=models.CharField(max_length=50,null=True,blank=True)
    cdesc2=models.CharField(max_length=500,null=True,blank=True)


class Homedata(models.Model):
   
    h1_desc=models.CharField(max_length=800)  
    h2_brief=models.CharField(max_length=255)
    
   
class Offerproduct(models.Model):
    oimg=models.ImageField(null=True, blank=True) 
    oproname=models.CharField(max_length=40)
    oprice=models.IntegerField()





    
class Sliderhome(models.Model):
    sheadng=models.CharField(max_length=30)  
    sdesc=models.CharField(max_length=255)
    simg=models.ImageField(null=True, blank=True)
    


class Contnt(models.Model):
    cheadng=models.CharField(max_length=40)  
    cdes=models.CharField(max_length=555)
   



@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            Admin.objects.create(admin=instance)
        if instance.user_type==2:
            Customer.objects.create(admin=instance,address="")
       

@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.admin.save()
    if instance.user_type==2:
        instance.customer.save()
   




