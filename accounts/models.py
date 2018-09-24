from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_client=models.BooleanField(default=False)
    is_agent=models.BooleanField(default=False)
    email = models.EmailField()

class Client(models.Model):
    first_name = models.CharField(max_length=20)
    last_name= models.CharField(max_length=20)
    user = models.OneToOneField(User)
    phone= models.BigIntegerField()
    address= models.TextField(blank=True)
    occupation= models.CharField(max_length=50,blank=True)
    date_of_birth = models.DateField(blank=True,null=True)
    def __str__(self):
        return self.user.username

class Payment(models.Model):
    cost = models.IntegerField()
    days = models.IntegerField()
    payplan = models.CharField(max_length=50)
    def __str__(self):
        return self.payplan


class Agent(models.Model):
    user = models.OneToOneField(Client)
    pend = models.IntegerField(default=0)
    complete_tour =models.IntegerField(default=0)
    complete_hotel =models.IntegerField(default=0)
    complete_train =models.IntegerField(default=0)
    complete_air =models.IntegerField(default=0)
    complete_bus =models.IntegerField(default=0)
    complete_visa =models.IntegerField(default=0)
    complete_car =models.IntegerField(default=0)
    complete_insrnce =models.IntegerField(default=0)
    complete_all =models.IntegerField(default=0)
    company_name=models.CharField(max_length=50,blank=True)
    payment_plan=models.ForeignKey(Payment,blank=True,null=True)
    paydate=models.DateTimeField(blank=True,null=True)
    expdate=models.DateTimeField(blank=True,null=True)
    rating=models.FloatField(blank=True,null=True)
    rated=models.IntegerField(default=0)
    def __str__(self):
        return self.user.user.username
