from django.db import models
from client.models import EnqTour, EnqHotel, EnqTrain, EnqAir, EnqBus, EnqVisa, EnqCar, EnqInsrnce
from accounts.models import Agent
# Create your models here.


class EnqTourReply(models.Model):
    enq = models.ForeignKey(EnqTour,related_name='tourreply',on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent,related_name='tourpending')
    names_of_cities=models.TextField()
    budget=models.CharField(max_length=15)
    additional_information=models.TextField(blank=True,null=True)
    replied = models.DateTimeField(auto_now_add=True)

class EnqHotelReply(models.Model):
    enq = models.ForeignKey(EnqHotel,related_name='hotelreply',on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent,related_name='hotelpending')
    names_of_hotels=models.TextField()
    prices_of_hotels=models.TextField()
    location_of_hotels=models.TextField()
    additional_information=models.TextField(blank=True,null=True)
    replied = models.DateTimeField(auto_now_add=True)

class EnqTrainReply(models.Model):
    enq = models.ForeignKey(EnqTrain,related_name='trainreply',on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent,related_name='trainpending')
    names_of_trains=models.TextField()
    train_timings=models.TextField()
    days_of_running=models.TextField()
    fares=models.TextField()
    additional_information=models.TextField(blank=True,null=True)
    replied = models.DateTimeField(auto_now_add=True)


class EnqAirReply(models.Model):
    enq = models.ForeignKey(EnqAir,related_name='airreply',on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent,related_name='airpending')
    flight_names=models.TextField()
    dates_and_timings=models.TextField()
    fares=models.TextField()
    additional_information=models.TextField(blank=True,null=True)
    replied = models.DateTimeField(auto_now_add=True)

class EnqBusReply(models.Model):
    enq = models.ForeignKey(EnqBus,related_name='busreply',on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent,related_name='buspending')
    bus_timings=models.TextField()
    fares=models.TextField()
    additional_information=models.TextField(blank=True,null=True)
    replied = models.DateTimeField(auto_now_add=True)

class EnqVisaReply(models.Model):
    enq = models.ForeignKey(EnqVisa,related_name='visareply',on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent,related_name='visapending')
    charges=models.CharField(max_length=50)
    additional_information=models.TextField(blank=True,null=True)
    replied = models.DateTimeField(auto_now_add=True)

class EnqCarReply(models.Model):
    enq = models.ForeignKey(EnqCar,related_name='carreply',on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent,related_name='carpending')
    vehicles_available=models.TextField()
    charges=models.TextField()
    additional_information=models.TextField(blank=True,null=True)
    replied = models.DateTimeField(auto_now_add=True)

class EnqInsrnceReply(models.Model):
    enq = models.ForeignKey(EnqInsrnce,related_name='insrncereply',on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent,related_name='insrncepending')
    insurance_coverage=models.TextField()
    charges=models.TextField()
    additional_information=models.TextField(blank=True,null=True)
    replied = models.DateTimeField(auto_now_add=True)
