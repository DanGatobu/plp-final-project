from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class inventory(models.Model):
    name = models.CharField(max_length=400)
    price = models.FloatField()
    category = models.CharField(max_length=400)
    location=models.CharField(max_length=400 ,default='Nairobi')
    image = models.ImageField(max_length=400, upload_to='images/')
    vendor = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    





class tempcart(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(inventory)
    
    
    datecreated = models.DateTimeField(auto_now_add=True)

class customerorder(models.Model):
    items = models.ManyToManyField(inventory)
    datecreated = models.DateTimeField(auto_now_add=True)
    totalprice = models.FloatField()
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
