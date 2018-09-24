from django.contrib import admin
from client.models import (TourType, TrainClass, FlightClass, BusClass, Service, Vehicle, Rating,
                            EnqTour, EnqHotel, EnqTrain, EnqAir, EnqBus, EnqVisa, EnqCar, EnqInsrnce,
                            EnqTourArchiv, EnqHotelArchiv, EnqTrainArchiv, EnqAirArchiv, EnqBusArchiv, EnqVisaArchiv, EnqCarArchiv, EnqInsrnceArchiv)
# Register your models here.
admin.site.register(TourType)
admin.site.register(TrainClass)
admin.site.register(FlightClass)
admin.site.register(BusClass)
admin.site.register(Service)
admin.site.register(Vehicle)
admin.site.register(Rating)

admin.site.register(EnqTour)
admin.site.register(EnqHotel)
admin.site.register(EnqTrain)
admin.site.register(EnqAir)
admin.site.register(EnqBus)
admin.site.register(EnqVisa)
admin.site.register(EnqCar)
admin.site.register(EnqInsrnce)

admin.site.register(EnqTourArchiv)
admin.site.register(EnqHotelArchiv)
admin.site.register(EnqTrainArchiv)
admin.site.register(EnqAirArchiv)
admin.site.register(EnqBusArchiv)
admin.site.register(EnqVisaArchiv)
admin.site.register(EnqCarArchiv)
admin.site.register(EnqInsrnceArchiv)
