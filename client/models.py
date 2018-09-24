from django.db import models
from accounts.models import Client, Agent

# Create your models here.
class TourType(models.Model):
    type=models.CharField(max_length=15)
    def __str__(self):
        return self.type

class TrainClass(models.Model):
    tclass=models.CharField(max_length=20)
    def __str__(self):
        return self.tclass

class FlightClass(models.Model):
    fclass=models.CharField(max_length=20)
    def __str__(self):
        return self.fclass

class BusClass(models.Model):
    bclass=models.CharField(max_length=20)
    def __str__(self):
        return self.bclass

class Service(models.Model):
    service=models.CharField(max_length=20)
    def __str__(self):
        return self.service

class Vehicle(models.Model):
    car=models.CharField(max_length=20)
    def __str__(self):
        return self.car

class Rating(models.Model):
    rate=models.CharField(max_length=15)
    stars=models.IntegerField()
    def __str__(self):
        return self.rate


#all the enquiries here....

class EnqTour(models.Model):
    client=models.ForeignKey(Client,related_name='enqtour',on_delete=models.CASCADE)
    country = models.CharField(max_length=20)
    cities_to_travel = models.TextField()
    tour_start_date=models.DateField()
    tour_end_date=models.DateField()
    maximum_price=models.CharField(max_length=15)
    minimum_price=models.CharField(max_length=15)
    number_of_adults=models.IntegerField()
    number_of_children=models.IntegerField(default=0)
    number_of_infants=models.IntegerField(default=0)
    additional_information=models.TextField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)

class EnqHotel(models.Model):
    client=models.ForeignKey(Client,related_name='enqhotel',on_delete=models.CASCADE)
    location = models.CharField(max_length=50)
    stay_from=models.DateField()
    stay_upto=models.DateField()
    number_of_adults=models.IntegerField()
    number_of_children=models.IntegerField(default=0)
    number_of_infants=models.IntegerField(default=0)
    maximum_price=models.CharField(max_length=15)
    minimum_price=models.CharField(max_length=15)
    number_of_rooms_required=models.IntegerField()
    additional_information=models.TextField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)

class EnqTrain(models.Model):
    client=models.ForeignKey(Client,related_name='enqtrain',on_delete=models.CASCADE)
    tour_type=models.ForeignKey(TourType)
    travel_start_location=models.CharField(max_length=20)
    destination=models.CharField(max_length=20)
    date_of_travel=models.DateField()
    number_of_adults=models.IntegerField()
    number_of_children=models.IntegerField(default=0)
    number_of_infants=models.IntegerField(default=0)
    catagory = models.ForeignKey(TrainClass)
    additional_information=models.TextField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)

class EnqAir(models.Model):
    client=models.ForeignKey(Client,related_name='enqair',on_delete=models.CASCADE)
    tour_type=models.ForeignKey(TourType)
    travel_start_location=models.CharField(max_length=20)
    destination=models.CharField(max_length=20)
    date_of_travel=models.DateField()
    number_of_adults=models.IntegerField()
    number_of_children=models.IntegerField(default=0)
    number_of_infants=models.IntegerField(default=0)
    catagory = models.ForeignKey(FlightClass)
    additional_information=models.TextField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)

class EnqBus(models.Model):
    client=models.ForeignKey(Client,related_name='enqbus',on_delete=models.CASCADE)
    tour_type=models.ForeignKey(TourType)
    travel_start_location=models.CharField(max_length=20)
    destination=models.CharField(max_length=20)
    date_of_travel=models.DateField()
    number_of_adults=models.IntegerField()
    number_of_children=models.IntegerField(default=0)
    number_of_infants=models.IntegerField(default=0)
    catagory = models.ForeignKey(BusClass)
    additional_information=models.TextField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)

class EnqVisa(models.Model):
    client=models.ForeignKey(Client,related_name='enqvisa',on_delete=models.CASCADE)
    service=models.ForeignKey(Service)
    additional_information=models.TextField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)

class EnqCar(models.Model):
    client=models.ForeignKey(Client,related_name='enqcar',on_delete=models.CASCADE)
    tour_type=models.ForeignKey(TourType)
    type_of_vehicle=models.ForeignKey(Vehicle)
    book_from=models.DateField()
    book_upto=models.DateField()
    travel_start_location=models.CharField(max_length=20)
    destination=models.CharField(max_length=20)
    number_of_vehicles_required=models.IntegerField()
    additional_information=models.TextField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)

class EnqInsrnce(models.Model):
    client=models.ForeignKey(Client,related_name='enqinsrnce',on_delete=models.CASCADE)
    country = models.CharField(max_length=20)
    type_of_insurance=models.CharField(max_length=30)
    number_of_people=models.IntegerField()
    ages_of_people=models.CharField(max_length=200)
    travel_start_location=models.CharField(max_length=20)
    destination=models.CharField(max_length=20)
    additional_information=models.TextField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)



#archives here....

class EnqTourArchiv(models.Model):
    client=models.ForeignKey(Client,related_name='enqtourarchiv')
    country = models.CharField(max_length=20)
    cities_to_travel = models.TextField()
    tour_start_date=models.DateField()
    tour_end_date=models.DateField()
    maximum_price=models.CharField(max_length=15)
    minimum_price=models.CharField(max_length=15)
    number_of_adults=models.IntegerField()
    number_of_children=models.IntegerField()
    number_of_infants=models.IntegerField()
    additional_information=models.TextField(blank=True,null=True)
    created = models.DateTimeField()
    agent = models.ForeignKey(Agent,related_name='tourdone')
    names_of_cities=models.TextField()
    budget=models.CharField(max_length=15)
    additional_information_reply=models.TextField(blank=True,null=True)
    replied = models.DateTimeField()
    accptd = models.DateTimeField(auto_now_add=True)
    rating=models.ForeignKey(Rating,blank=True,null=True)

class EnqHotelArchiv(models.Model):
    client=models.ForeignKey(Client,related_name='enqhotelarchiv')
    location = models.CharField(max_length=50)
    stay_from=models.DateField()
    stay_upto=models.DateField()
    number_of_adults=models.IntegerField()
    number_of_children=models.IntegerField()
    number_of_infants=models.IntegerField()
    maximum_price=models.CharField(max_length=15)
    minimum_price=models.CharField(max_length=15)
    number_of_rooms_required=models.IntegerField()
    additional_information=models.TextField(blank=True,null=True)
    created = models.DateTimeField()
    agent = models.ForeignKey(Agent,related_name='hoteldone')
    names_of_hotels=models.TextField()
    prices_of_hotels=models.TextField()
    location_of_hotels=models.TextField()
    additional_information_reply=models.TextField(blank=True,null=True)
    replied = models.DateTimeField()
    accptd = models.DateTimeField(auto_now_add=True)
    rating=models.ForeignKey(Rating,blank=True,null=True)

class EnqTrainArchiv(models.Model):
    client=models.ForeignKey(Client,related_name='enqtrainarchiv')
    tour_type=models.ForeignKey(TourType)
    travel_start_location=models.CharField(max_length=20)
    destination=models.CharField(max_length=20)
    date_of_travel=models.DateField()
    number_of_adults=models.IntegerField()
    number_of_children=models.IntegerField()
    number_of_infants=models.IntegerField()
    catagory = models.ForeignKey(TrainClass)
    additional_information=models.TextField(blank=True,null=True)
    created = models.DateTimeField()
    agent = models.ForeignKey(Agent,related_name='traindone')
    names_of_trains=models.TextField()
    train_timings=models.TextField()
    days_of_running=models.TextField()
    fares=models.TextField()
    additional_information_reply=models.TextField(blank=True,null=True)
    replied = models.DateTimeField()
    accptd = models.DateTimeField(auto_now_add=True)
    rating=models.ForeignKey(Rating,blank=True,null=True)

class EnqAirArchiv(models.Model):
    client=models.ForeignKey(Client,related_name='enqairarchiv')
    tour_type=models.ForeignKey(TourType)
    travel_start_location=models.CharField(max_length=20)
    destination=models.CharField(max_length=20)
    date_of_travel=models.DateField()
    number_of_adults=models.IntegerField()
    number_of_children=models.IntegerField()
    number_of_infants=models.IntegerField()
    catagory = models.ForeignKey(FlightClass)
    additional_information=models.TextField(blank=True,null=True)
    created = models.DateTimeField()
    agent = models.ForeignKey(Agent,related_name='airdone')
    flight_names=models.TextField()
    dates_and_timings=models.TextField()
    fares=models.TextField()
    additional_information_reply=models.TextField(blank=True,null=True)
    replied = models.DateTimeField()
    accptd = models.DateTimeField(auto_now_add=True)
    rating=models.ForeignKey(Rating,blank=True,null=True)

class EnqBusArchiv(models.Model):
    client=models.ForeignKey(Client,related_name='enqbusarchiv')
    tour_type=models.ForeignKey(TourType)
    travel_start_location=models.CharField(max_length=20)
    destination=models.CharField(max_length=20)
    date_of_travel=models.DateField()
    number_of_adults=models.IntegerField()
    number_of_children=models.IntegerField()
    number_of_infants=models.IntegerField()
    catagory = models.ForeignKey(BusClass)
    additional_information=models.TextField(blank=True,null=True)
    created = models.DateTimeField()
    agent = models.ForeignKey(Agent,related_name='busdone')
    bus_timings=models.TextField()
    fares=models.TextField()
    additional_information_reply=models.TextField(blank=True,null=True)
    replied = models.DateTimeField()
    accptd = models.DateTimeField(auto_now_add=True)
    rating=models.ForeignKey(Rating,blank=True,null=True)

class EnqVisaArchiv(models.Model):
    client=models.ForeignKey(Client,related_name='enqvisaarchiv')
    service=models.ForeignKey(Service)
    additional_information=models.TextField(blank=True,null=True)
    created = models.DateTimeField()
    agent = models.ForeignKey(Agent,related_name='visadone')
    charges=models.CharField(max_length=50)
    additional_information_reply=models.TextField(blank=True,null=True)
    replied = models.DateTimeField()
    accptd = models.DateTimeField(auto_now_add=True)
    rating=models.ForeignKey(Rating,blank=True,null=True)

class EnqCarArchiv(models.Model):
    client=models.ForeignKey(Client,related_name='enqcararchiv')
    tour_type=models.ForeignKey(TourType)
    type_of_vehicle=models.ForeignKey(Vehicle)
    book_from=models.DateField()
    book_upto=models.DateField()
    travel_start_location=models.CharField(max_length=20)
    destination=models.CharField(max_length=20)
    number_of_vehicles_required=models.IntegerField()
    additional_information=models.TextField(blank=True,null=True)
    created = models.DateTimeField()
    agent = models.ForeignKey(Agent,related_name='cardone')
    vehicles_available=models.TextField()
    charges=models.TextField()
    additional_information_reply=models.TextField(blank=True,null=True)
    replied = models.DateTimeField()
    accptd = models.DateTimeField(auto_now_add=True)
    rating=models.ForeignKey(Rating,blank=True,null=True)

class EnqInsrnceArchiv(models.Model):
    client=models.ForeignKey(Client,related_name='enqinsrncearchiv')
    country = models.CharField(max_length=20)
    type_of_insurance=models.CharField(max_length=30)
    number_of_people=models.IntegerField()
    ages_of_people=models.CharField(max_length=200)
    travel_start_location=models.CharField(max_length=20)
    destination=models.CharField(max_length=20)
    additional_information=models.TextField(blank=True,null=True)
    created = models.DateTimeField()
    agent = models.ForeignKey(Agent,related_name='insrncedone')
    insurance_coverage=models.TextField()
    charges=models.TextField()
    additional_information_reply=models.TextField(blank=True,null=True)
    replied = models.DateTimeField()
    accptd = models.DateTimeField(auto_now_add=True)
    rating=models.ForeignKey(Rating,blank=True,null=True)
