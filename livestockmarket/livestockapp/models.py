from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class inventory(models.Model):
    name = models.CharField(max_length=400)
    price = models.FloatField()
    amount = models.IntegerField()
    category = models.CharField(max_length=400)
    image = models.ImageField(max_length=400, upload_to='images/')
    vendor = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
class course(models.Model):
    name = models.CharField(max_length=255)
    course_description = models.TextField()
    course_material = models.FileField(upload_to='course_material/')
    video = models.FileField(upload_to='course_videos/')

    def __str__(self):
        return self.name



class customerorder(models.Model):
    items = models.ManyToManyField(inventory)
    datecreated = models.DateTimeField(auto_now_add=True)
    totalprice = models.FloatField()
    owner=models.ForeignKey(User,on_delete=models.CASCADE)

class tempcart(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(inventory)
    datecreated = models.DateTimeField(auto_now_add=True)

class suppliments(models.Model):
    name=models.CharField(max_length=100)
    price=models.FloatField()
    ammount=models.IntegerField()
    image=models.ImageField(upload_to='suppliment_image/')
