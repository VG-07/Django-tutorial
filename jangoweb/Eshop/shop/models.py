

from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=25)


    def __str__(self) :
        return self.name
    

class ProductManager(models.Manager):
    def get_products_by_category_id(self, category_id=None):
        if category_id:
            return self.filter(category_id=category_id)
        else:
            return self.all()



class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default="", null=True, blank= True)
    image = models.ImageField(upload_to="upload/product")
    quantity = models.PositiveIntegerField(default=1)
    objects = ProductManager()

# @staticmethod
# def get_all_Product():
#     return Product.objects.all()

# @classmethod
# def get_all_Product(cls):
#     return cls.objects.all()
    
# @staticmethod
# def get_all_products_by_categoryid(category_id):
#     if category_id:
#         return Product.objects.filter(category = category_id )
#     else:
#         return Product.objects.all()

class Customer (models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    phone = models.CharField(max_length=15)
    email= models.EmailField()
    password = models.CharField(max_length=500)

    def register(self):
         self.save()

    @staticmethod
    def get_customer_by_email(email): # for log in email verification 
        try:
            return Customer.objects.get(email = email) # i am cant use filer becouser filter get all list but we require onely one 
        except:
            return False
        
        
    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False
    
# class CartItem(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     quantity = models.PositiveIntegerField(default=1)
#     price = models.DecimalField(max_digits=10, decimal_places=2)