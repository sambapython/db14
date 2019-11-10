from django.db import models

# Create your models here.
class Category(models.Model):
	name=models.CharField(max_length=250)

class Product(models.Model):
	name= models.CharField(max_length=250)
	category = models.ForeignKey(Category, on_delete=models.PROTECT)
	description = models.TextField(max_length=600)
class Transaction(models.Model):
	types = [("in","STOCK IN"),("out","STOCK OUT")]
	product = models.ForeignKey(Product,on_delete=models.PROTECT)
	quantity = models.IntegerField(default=1)
	type= models.CharField(choices=types,max_length=3)
	description = models.TextField(max_length=600)

