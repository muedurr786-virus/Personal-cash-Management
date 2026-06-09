from django.db import models
from django.contrib.auth.models import AbstractUser


class UserCreate(AbstractUser):
    
    def __str__(self):
        return self.username
    
class ProfileModel(models.Model):
    user = models.OneToOneField(UserCreate, on_delete=models.CASCADE)
    occupation = models.CharField(null=True, max_length=250)
    full_name = models.CharField(null=True, max_length=250)
    address = models.TextField(null=True)
    image = models.ImageField(null=True, upload_to='media/image')
    
    
    def __str__(self):
        return self.full_name
    

class AddcashModel(models.Model):
    user = models.ForeignKey(UserCreate, on_delete=models.CASCADE)
    amount = models.IntegerField(null=True)
    source = models.CharField(null=True, max_length=250)
    description = models.CharField(null=True, max_length=250)
    date = models.DateField(null=True, auto_now_add=True)
    
    def __str__(self):
        return self.amount
    
class ExpaendModel(models.Model):
    user = models.ForeignKey(UserCreate, on_delete=models.CASCADE)
    amount = models.IntegerField(null=True)
    description = models.CharField(null=True, max_length=250)
    date = models.DateTimeField(null=True, auto_now_add=True)
    
    
    def __str__(self):
        return self.amount  
    
