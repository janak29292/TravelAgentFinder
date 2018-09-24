from django.shortcuts import render,get_object_or_404,get_list_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from client.forms import (UserForm, ClientForm, EnqTourForm, EnqHotelForm, EnqTrainForm, EnqAirForm, EnqBusForm, EnqVisaForm, EnqCarForm, EnqInsrnceForm,
                            TourRating, HotelRating, TrainRating, AirRating, BusRating, VisaRating, CarRating, InsrnceRating )
from accounts.decorators import client_required
from accounts.models import Agent, Client
from client.models import (EnqTour, EnqHotel, EnqTrain, EnqAir, EnqBus, EnqVisa, EnqCar, EnqInsrnce,
                            EnqTourArchiv, EnqHotelArchiv, EnqTrainArchiv, EnqAirArchiv, EnqBusArchiv, EnqVisaArchiv, EnqCarArchiv, EnqInsrnceArchiv)
from agent.models import EnqTourReply, EnqHotelReply, EnqTrainReply, EnqAirReply, EnqBusReply, EnqVisaReply, EnqCarReply, EnqInsrnceReply

# Create your views here.
# @login_required
# @client_required
# def clientdash(request):
#     return render(request,'client/enqtourlist.html',{'insertme':'My Account'})

def clientsignup(request):
    er=''
    registered = False

    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)
        client_form = ClientForm(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid() and client_form.is_valid():

            # Save User Form to Database
            user = user_form.save(commit=False)
            user.is_client = True

            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            user.save()

            # Now we deal with the extra info!
            client = client_form.save(commit=False)
            # Can't commit yet because we still need to manipulate
            client.user = user
            client.save()
            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            # raise client_form.errors
            user_form = UserForm()
            client_form = ClientForm()
            er = 'Registration Failed'
    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form= UserForm()
        client_form = ClientForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'client/signup.html',
                          {'user_form':user_form,
                            'client_form':client_form,
                           'registered':registered,
                           'insertme':'Client SignUp',
                           'er':er})

@login_required
@client_required
def enqtour(request):
    registered = False
    if request.method=='POST':
        enqtourform = EnqTourForm(data=request.POST)
        if enqtourform.is_valid():
            enqtour = enqtourform.save(commit=False)
            enqtour.client = get_object_or_404(Client,user=request.user)
            enqtour.save()
            registered=True
        else:
            enqtourform = EnqTourForm()
    else:
        enqtourform = EnqTourForm()
    return render(request,'client/enqtourform.html',{'enqtourform':enqtourform,'registered':registered,'insertme':'Client : '+str(request.user),'acc':'acc'})

@login_required
@client_required
def enqtourlist(request):
    list= [a for a in EnqTour.objects.all() if a.client == get_object_or_404(Client,user=request.user)]
    return render(request,'client/enqtourlist.html',{'list':list,'insertme':'Client : '+str(request.user),'acc':'acc'})

@login_required
@client_required
def clienttouraccpt(request,enq,acpt):
    enqobj = get_object_or_404(EnqTour,pk=enq)
    acptobj=get_object_or_404(EnqTourReply,pk=acpt)
    tourarch = EnqTourArchiv(client=enqobj.client,
                                    country=enqobj.country,
                                    cities_to_travel=enqobj.cities_to_travel,
                                    tour_start_date=enqobj.tour_start_date,
                                    tour_end_date=enqobj.tour_end_date,
                                    maximum_price=enqobj.maximum_price,
                                    minimum_price=enqobj.minimum_price,
                                    number_of_adults=enqobj.number_of_adults,
                                    number_of_children=enqobj.number_of_children,
                                    number_of_infants=enqobj.number_of_infants,
                                    additional_information=enqobj.additional_information,
                                    created=enqobj.created,
                                    agent=acptobj.agent,
                                    names_of_cities=acptobj.names_of_cities,
                                    budget=acptobj.budget,
                                    additional_information_reply=acptobj.additional_information,
                                    replied=acptobj.replied)
    agrt=get_object_or_404(Agent,pk=acptobj.agent.pk)
    agrt.pend-=1
    agrt.complete_tour+=1
    agrt.complete_all+=1
    agrt.save()
    tourarch.save()
    enqobj.delete()
    return HttpResponseRedirect(reverse('client:enqtourlist'))

@login_required
@client_required
def enqtourdone(request):
    dlist=[a for a in EnqTourArchiv.objects.all() if a.client == get_object_or_404(Client,user=request.user)]
    return render(request,'client/enqtourarch.html',{'dlist':dlist,'insertme':'Client : '+str(request.user),'acc':'acc'})

@login_required
@client_required
def enqtourdel(request,key):
    enqobj = get_object_or_404(EnqTour,pk=key)
    rpobj = get_list_or_404(EnqTourReply,enq=enqobj)
    for a in rpobj:
        agrp=get_object_or_404(Agent,pk=a.agent.pk)
        agrp.pend-=1
        agrp.save()
    enqobj.delete()
    return HttpResponseRedirect(reverse('client:enqtourlist'))

@login_required
@client_required
def tourrate(request,arch):
    registered=False
    if request.method=='POST':
        form =TourRating(request.POST)
        if form.is_valid():
            rate = form.cleaned_data['rating']
            a = get_object_or_404(EnqTourArchiv,pk=arch)
            a.rating = rate
            a.save()
            ag = get_object_or_404(Agent,pk=a.agent.pk)
            if ag.rating:
                ag.rating=(ag.rated*ag.rating+rate.stars)/(ag.rated+1)
                ag.rated+=1
            else:
                ag.rating=rate.stars
                ag.rated+=1
            ag.save()
            registered=True
    else:
        form = TourRating()
    return render(request,'client/tourrate.html',{'form':form,'registered':registered,'rte':rate.stars})



@login_required
@client_required
def enqhotel(request):
    registered = False
    if request.method=='POST':
        enqhotelform = EnqHotelForm(data=request.POST)
        if enqhotelform.is_valid():
            enqhotel = enqhotelform.save(commit=False)
            enqhotel.client = get_object_or_404(Client,user=request.user)
            enqhotel.save()
            registered=True
        else:
            enqhotelform = EnqHotelForm()
    else:
        enqhotelform = EnqHotelForm()
    return render(request,'client/enqhotelform.html',{'enqhotelform':enqhotelform,'registered':registered,'insertme':'Client : '+str(request.user),'acc':'acc'})

@login_required
@client_required
def enqhotellist(request):
    list= [a for a in EnqHotel.objects.all() if a.client == get_object_or_404(Client,user=request.user)]
    return render(request,'client/enqhotellist.html',{'list':list,'insertme':'Client : '+str(request.user),'acc':'acc'})

@login_required
@client_required
def clienthotelaccpt(request,enq,acpt):
    enqobj = get_object_or_404(EnqHotel,pk=enq)
    acptobj=get_object_or_404(EnqHotelReply,pk=acpt)
    hotelarch = EnqHotelArchiv(client=enqobj.client,
                                    location=enqobj.location,
                                    stay_from=enqobj.stay_from,
                                    stay_upto=enqobj.stay_upto,
                                    number_of_adults=enqobj.number_of_adults,
                                    number_of_children=enqobj.number_of_children,
                                    number_of_infants=enqobj.number_of_infants,
                                    maximum_price=enqobj.maximum_price,
                                    minimum_price=enqobj.minimum_price,
                                    number_of_rooms_required=enqobj.number_of_rooms_required,
                                    additional_information=enqobj.additional_information,
                                    created=enqobj.created,
                                    agent=acptobj.agent,
                                    names_of_hotels=acptobj.names_of_hotels,
                                    prices_of_hotels=acptobj.prices_of_hotels,
                                    location_of_hotels=acptobj.location_of_hotels,
                                    additional_information_reply=acptobj.additional_information,
                                    replied=acptobj.replied)
    agrt=get_object_or_404(Agent,pk=acptobj.agent.pk)
    agrt.pend-=1
    agrt.complete_hotel+=1
    agrt.complete_all+=1
    agrt.save()
    hotelarch.save()
    enqobj.delete()
    return HttpResponseRedirect(reverse('client:enqhotellist'))

@login_required
@client_required
def enqhoteldone(request):
    dlist=[a for a in EnqHotelArchiv.objects.all() if a.client == get_object_or_404(Client,user=request.user)]
    return render(request,'client/enqhotelarch.html',{'dlist':dlist,'insertme':'Client : '+str(request.user),'acc':'acc'})

@login_required
@client_required
def enqhoteldel(request,key):
    enqobj = get_object_or_404(EnqHotel,pk=key)
    rpobj = get_list_or_404(EnqHotelReply,enq=enqobj)
    for a in rpobj:
        agrp=get_object_or_404(Agent,pk=a.agent.pk)
        agrp.pend-=1
        agrp.save()
    enqobj.delete()
    return HttpResponseRedirect(reverse('client:enqhotellist'))

@login_required
@client_required
def hotelrate(request,arch):
    registered=False
    rate=None
    rte=None
    if request.method=='POST':
        form =HotelRating(request.POST)
        if form.is_valid():
            rate = form.cleaned_data['rating']
            rte=rate.stars
            a = get_object_or_404(EnqHotelArchiv,pk=arch)
            a.rating = rate
            a.save()
            ag = get_object_or_404(Agent,pk=a.agent.pk)
            if ag.rating:
                ag.rating=(ag.rated*ag.rating+rate.stars)/(ag.rated+1)
                ag.rated+=1
            else:
                ag.rating=rate.stars
                ag.rated+=1
                ag.rated+=1
            ag.save()
            registered=True
    else:
        form = HotelRating()
    return render(request,'client/hotelrate.html',{'form':form,'registered':registered,'rte':rte})



@login_required
@client_required
def enqtrain(request):
    registered = False
    if request.method=='POST':
        enqtrainform = EnqTrainForm(data=request.POST)
        if enqtrainform.is_valid():
            enqtrain = enqtrainform.save(commit=False)
            enqtrain.client = get_object_or_404(Client,user=request.user)
            enqtrain.save()
            registered=True
        else:
            enqtrainform = EnqTrainForm()
    else:
        enqtrainform = EnqTrainForm()
    return render(request,'client/enqtrainform.html',{'enqtrainform':enqtrainform,'registered':registered,'insertme':'Client : '+str(request.user),'acc':'acc'})

@login_required
@client_required
def enqtrainlist(request):
    list= [a for a in EnqTrain.objects.all() if a.client == get_object_or_404(Client,user=request.user)]
    return render(request,'client/enqtrainlist.html',{'list':list,'insertme':'Client : '+str(request.user),'acc':'acc'})

@login_required
@client_required
def clienttrainaccpt(request,enq,acpt):
    enqobj = get_object_or_404(EnqTrain,pk=enq)
    acptobj=get_object_or_404(EnqTrainReply,pk=acpt)
    trainarch = EnqTrainArchiv(client=enqobj.client,
                                    tour_type=enqobj.tour_type,
                                    travel_start_location=enqobj.travel_start_location,
                                    destination=enqobj.destination,
                                    date_of_travel=enqobj.date_of_travel,
                                    number_of_adults=enqobj.number_of_adults,
                                    number_of_children=enqobj.number_of_children,
                                    number_of_infants=enqobj.number_of_infants,
                                    catagory=enqobj.catagory,
                                    additional_information=enqobj.additional_information,
                                    created=enqobj.created,
                                    agent=acptobj.agent,
                                    names_of_trains=acptobj.names_of_trains,
                                    train_timings=acptobj.train_timings,
                                    days_of_running=acptobj.days_of_running,
                                    fares=acptobj.fares,
                                    additional_information_reply=acptobj.additional_information,
                                    replied=acptobj.replied)
    agrt=get_object_or_404(Agent,pk=acptobj.agent.pk)
    agrt.pend-=1
    agrt.complete_train+=1
    agrt.complete_all+=1
    agrt.save()
    trainarch.save()
    enqobj.delete()
    return HttpResponseRedirect(reverse('client:enqtrainlist'))

@login_required
@client_required
def enqtraindone(request):
    dlist=[a for a in EnqTrainArchiv.objects.all() if a.client == get_object_or_404(Client,user=request.user)]
    return render(request,'client/enqtrainarch.html',{'dlist':dlist,'insertme':'Client : '+str(request.user),'acc':'acc'})

@login_required
@client_required
def enqtraindel(request,key):
    enqobj = get_object_or_404(EnqTrain,pk=key)
    rpobj = get_list_or_404(EnqTrainReply,enq=enqobj)
    for a in rpobj:
        agrp=get_object_or_404(Agent,pk=a.agent.pk)
        agrp.pend-=1
        agrp.save()
    enqobj.delete()
    return HttpResponseRedirect(reverse('client:enqtrainlist'))

@login_required
@client_required
def trainrate(request,arch):
    registered=False
    if request.method=='POST':
        form =TrainRating(request.POST)
        if form.is_valid():
            rate = form.cleaned_data['rating']
            a = get_object_or_404(EnqTrainArchiv,pk=arch)
            a.rating = rate
            a.save()
            ag = get_object_or_404(Agent,pk=a.agent.pk)
            if ag.rating:
                ag.rating=(ag.rated*ag.rating+rate.stars)/(ag.rated+1)
                ag.rated+=1
            else:
                ag.rating=rate.stars
                ag.rated+=1
            ag.save()
            registered=True
    else:
        form = TrainRating()
    return render(request,'client/trainrate.html',{'form':form,'registered':registered,'rte':rate.stars})



@login_required
@client_required
def enqair(request):
    registered = False
    if request.method=='POST':
        enqairform = EnqAirForm(data=request.POST)
        if enqairform.is_valid():
            enqair = enqairform.save(commit=False)
            enqair.client = get_object_or_404(Client,user=request.user)
            enqair.save()
            registered=True
        else:
            enqairform = EnqAirForm()
    else:
        enqairform = EnqAirForm()
    return render(request,'client/enqairform.html',{'enqairform':enqairform,'registered':registered,'insertme':'Client : '+str(request.user),'acc':'acc'})

@login_required
@client_required
def enqairlist(request):
    list= [a for a in EnqAir.objects.all() if a.client == get_object_or_404(Client,user=request.user)]
    return render(request,'client/enqairlist.html',{'list':list,'insertme':'Client : '+str(request.user),'acc':'acc'})

@login_required
@client_required
def clientairaccpt(request,enq,acpt):
    enqobj = get_object_or_404(EnqAir,pk=enq)
    acptobj=get_object_or_404(EnqAirReply,pk=acpt)
    airarch = EnqAirArchiv(client=enqobj.client,
                                    tour_type=enqobj.tour_type,
                                    travel_start_location=enqobj.travel_start_location,
                                    destination=enqobj.destination,
                                    date_of_travel=enqobj.date_of_travel,
                                    number_of_adults=enqobj.number_of_adults,
                                    number_of_children=enqobj.number_of_children,
                                    number_of_infants=enqobj.number_of_infants,
                                    catagory=enqobj.catagory,
                                    additional_information=enqobj.additional_information,
                                    created=enqobj.created,
                                    agent=acptobj.agent,
                                    flight_names=acptobj.flight_names,
                                    train_timings=acptobj.train_timings,
                                    dates_and_timings=acptobj.dates_and_timings,
                                    fares=acptobj.fares,
                                    additional_information_reply=acptobj.additional_information,
                                    replied=acptobj.replied)
    agrt=get_object_or_404(Agent,pk=acptobj.agent.pk)
    agrt.pend-=1
    agrt.complete_air+=1
    agrt.complete_all+=1
    agrt.save()
    airarch.save()
    enqobj.delete()
    return HttpResponseRedirect(reverse('client:enqairlist'))

@login_required
@client_required
def enqairdone(request):
    dlist=[a for a in EnqAirArchiv.objects.all() if a.client == get_object_or_404(Client,user=request.user)]
    return render(request,'client/enqairarch.html',{'dlist':dlist,'insertme':'Client : '+str(request.user),'acc':'acc'})

@login_required
@client_required
def enqairdel(request,key):
    enqobj = get_object_or_404(EnqAir,pk=key)
    rpobj = get_list_or_404(EnqAirReply,enq=enqobj)
    for a in rpobj:
        agrp=get_object_or_404(Agent,pk=a.agent.pk)
        agrp.pend-=1
        agrp.save()
    enqobj.delete()
    return HttpResponseRedirect(reverse('client:enqairlist'))

@login_required
@client_required
def airrate(request,arch):
    registered=False
    if request.method=='POST':
        form =AirRating(request.POST)
        if form.is_valid():
            rate = form.cleaned_data['rating']
            a = get_object_or_404(EnqAirArchiv,pk=arch)
            a.rating = rate
            a.save()
            ag = get_object_or_404(Agent,pk=a.agent.pk)
            if ag.rating:
                ag.rating=(ag.rated*ag.rating+rate.stars)/(ag.rated+1)
                ag.rated+=1
            else:
                ag.rating=rate.stars
                ag.rated+=1
            ag.save()
            registered=True
    else:
        form = AirRating()
    return render(request,'client/airrate.html',{'form':form,'registered':registered,'rte':rate.stars})



@login_required
@client_required
def enqbus(request):
    registered = False
    if request.method=='POST':
        enqbusform = EnqBusForm(data=request.POST)
        if enqbusform.is_valid():
            enqbus = enqbusform.save(commit=False)
            enqbus.client = get_object_or_404(Client,user=request.user)
            enqbus.save()
            registered=True
        else:
            enqbusform = EnqBusForm()
    else:
        enqbusform = EnqBusForm()
    return render(request,'client/enqbusform.html',{'enqbusform':enqbusform,'registered':registered,'insertme':'Client : '+str(request.user),'acc':'acc'})

@login_required
@client_required
def enqbuslist(request):
    list= [a for a in EnqBus.objects.all() if a.client == get_object_or_404(Client,user=request.user)]
    return render(request,'client/enqbuslist.html',{'list':list,'insertme':'Client : '+str(request.user),'acc':'acc'})

@login_required
@client_required
def clientbusaccpt(request,enq,acpt):
    enqobj = get_object_or_404(EnqBus,pk=enq)
    acptobj=get_object_or_404(EnqBusReply,pk=acpt)
    busarch = EnqBusArchiv(client=enqobj.client,
                                    tour_type=enqobj.tour_type,
                                    travel_start_location=enqobj.travel_start_location,
                                    destination=enqobj.destination,
                                    date_of_travel=enqobj.date_of_travel,
                                    number_of_adults=enqobj.number_of_adults,
                                    number_of_children=enqobj.number_of_children,
                                    number_of_infants=enqobj.number_of_infants,
                                    catagory=enqobj.catagory,
                                    additional_information=enqobj.additional_information,
                                    created=enqobj.created,
                                    agent=acptobj.agent,
                                    bus_timings=acptobj.bus_timings,
                                    fares=acptobj.fares,
                                    additional_information_reply=acptobj.additional_information,
                                    replied=acptobj.replied)
    agrt=get_object_or_404(Agent,pk=acptobj.agent.pk)
    agrt.pend-=1
    agrt.complete_bus+=1
    agrt.complete_all+=1
    agrt.save()
    busarch.save()
    enqobj.delete()
    return HttpResponseRedirect(reverse('client:enqbuslist'))

@login_required
@client_required
def enqbusdone(request):
    dlist=[a for a in EnqBusArchiv.objects.all() if a.client == get_object_or_404(Client,user=request.user)]
    return render(request,'client/enqbusarch.html',{'dlist':dlist,'insertme':'Client : '+str(request.user),'acc':'acc'})

@login_required
@client_required
def enqbusdel(request,key):
    enqobj = get_object_or_404(EnqBus,pk=key)
    rpobj = get_list_or_404(EnqBusReply,enq=enqobj)
    for a in rpobj:
        agrp=get_object_or_404(Agent,pk=a.agent.pk)
        agrp.pend-=1
        agrp.save()
    enqobj.delete()
    return HttpResponseRedirect(reverse('client:enqbuslist'))

@login_required
@client_required
def busrate(request,arch):
    registered=False
    if request.method=='POST':
        form =BusRating(request.POST)
        if form.is_valid():
            rate = form.cleaned_data['rating']
            a = get_object_or_404(EnqBusArchiv,pk=arch)
            a.rating = rate
            a.save()
            ag = get_object_or_404(Agent,pk=a.agent.pk)
            if ag.rating:
                ag.rating=(ag.rated*ag.rating+rate.stars)/(ag.rated+1)
                ag.rated+=1
            else:
                ag.rating=rate.stars
                ag.rated+=1
            ag.save()
            registered=True
    else:
        form = BusRating()
    return render(request,'client/busrate.html',{'form':form,'registered':registered,'rte':rate.stars})



@login_required
@client_required
def enqvisa(request):
    registered = False
    if request.method=='POST':
        enqvisaform = EnqVisaForm(data=request.POST)
        if enqvisaform.is_valid():
            enqvisa = enqvisaform.save(commit=False)
            enqvisa.client = get_object_or_404(Client,user=request.user)
            enqvisa.save()
            registered=True
        else:
            enqvisaform = EnqVisaForm()
    else:
        enqvisaform = EnqVisaForm()
    return render(request,'client/enqvisaform.html',{'enqvisaform':enqvisaform,'registered':registered,'insertme':'Client : '+str(request.user),'acc':'acc'})

@login_required
@client_required
def enqvisalist(request):
    list= [a for a in EnqVisa.objects.all() if a.client == get_object_or_404(Client,user=request.user)]
    return render(request,'client/enqvisalist.html',{'list':list,'insertme':'Client : '+str(request.user),'acc':'acc'})

@login_required
@client_required
def clientvisaaccpt(request,enq,acpt):
    enqobj = get_object_or_404(EnqVisa,pk=enq)
    acptobj=get_object_or_404(EnqVisaReply,pk=acpt)
    visaarch = EnqVisaArchiv(client=enqobj.client,
                                    service=enqobj.service,
                                    additional_information=enqobj.additional_information,
                                    created=enqobj.created,
                                    agent=acptobj.agent,
                                    charges=acptobj.charges,
                                    additional_information_reply=acptobj.additional_information,
                                    replied=acptobj.replied)
    agrt=get_object_or_404(Agent,pk=acptobj.agent.pk)
    agrt.pend-=1
    agrt.complete_visa+=1
    agrt.complete_all+=1
    agrt.save()
    visaarch.save()
    enqobj.delete()
    return HttpResponseRedirect(reverse('client:enqvisalist'))

@login_required
@client_required
def enqvisadone(request):
    dlist=[a for a in EnqVisaArchiv.objects.all() if a.client == get_object_or_404(Client,user=request.user)]
    return render(request,'client/enqvisaarch.html',{'dlist':dlist,'insertme':'Client : '+str(request.user),'acc':'acc'})

@login_required
@client_required
def enqvisadel(request,key):
    enqobj = get_object_or_404(EnqVisa,pk=key)
    rpobj = get_list_or_404(EnqVisaReply,enq=enqobj)
    for a in rpobj:
        agrp=get_object_or_404(Agent,pk=a.agent.pk)
        agrp.pend-=1
        agrp.save()
    enqobj.delete()
    return HttpResponseRedirect(reverse('client:enqvisalist'))

@login_required
@client_required
def visarate(request,arch):
    registered=False
    if request.method=='POST':
        form =VisaRating(request.POST)
        if form.is_valid():
            rate = form.cleaned_data['rating']
            a = get_object_or_404(EnqVisaArchiv,pk=arch)
            a.rating = rate
            a.save()
            ag = get_object_or_404(Agent,pk=a.agent.pk)
            if ag.rating:
                ag.rating=(ag.rated*ag.rating+rate.stars)/(ag.rated+1)
                ag.rated+=1
            else:
                ag.rating=rate.stars
                ag.rated+=1
            ag.save()
            registered=True
    else:
        form = VisaRating()
    return render(request,'client/visarate.html',{'form':form,'registered':registered,'rte':rate.stars})



@login_required
@client_required
def enqcar(request):
    registered = False
    if request.method=='POST':
        enqcarform = EnqCarForm(data=request.POST)
        if enqcarform.is_valid():
            enqcar = enqcarform.save(commit=False)
            enqcar.client = get_object_or_404(Client,user=request.user)
            enqcar.save()
            registered=True
        else:
            enqcarform = EnqCarForm()
    else:
        enqcarform = EnqCarForm()
    return render(request,'client/enqcarform.html',{'enqcarform':enqcarform,'registered':registered,'insertme':'Client : '+str(request.user),'acc':'acc'})

@login_required
@client_required
def enqcarlist(request):
    list= [a for a in EnqCar.objects.all() if a.client == get_object_or_404(Client,user=request.user)]
    return render(request,'client/enqcarlist.html',{'list':list,'insertme':'Client : '+str(request.user),'acc':'acc'})

@login_required
@client_required
def clientcaraccpt(request,enq,acpt):
    enqobj = get_object_or_404(EnqCar,pk=enq)
    acptobj=get_object_or_404(EnqCarReply,pk=acpt)
    cararch = EnqCarArchiv(client=enqobj.client,
                                    tour_type=enqobj.tour_type,
                                    type_of_vehicle=enqobj.type_of_vehicle,
                                    book_from=enqobj.book_from,
                                    book_upto=enqobj.book_upto,
                                    travel_start_location=enqobj.travel_start_location,
                                    destination=enqobj.destination,
                                    number_of_vehicles_required=enqobj.number_of_vehicles_required,
                                    additional_information=enqobj.additional_information,
                                    created=enqobj.created,
                                    agent=acptobj.agent,
                                    vehicles_available=acptobj.vehicles_available,
                                    charges=acptobj.charges,
                                    additional_information_reply=acptobj.additional_information,
                                    replied=acptobj.replied)
    agrt=get_object_or_404(Agent,pk=acptobj.agent.pk)
    agrt.pend-=1
    agrt.complete_car+=1
    agrt.complete_all+=1
    agrt.save()
    cararch.save()
    enqobj.delete()
    return HttpResponseRedirect(reverse('client:enqcarlist'))

@login_required
@client_required
def enqcardone(request):
    dlist=[a for a in EnqCarArchiv.objects.all() if a.client == get_object_or_404(Client,user=request.user)]
    return render(request,'client/enqcararch.html',{'dlist':dlist,'insertme':'Client : '+str(request.user),'acc':'acc'})

@login_required
@client_required
def enqcardel(request,key):
    enqobj = get_object_or_404(EnqCar,pk=key)
    rpobj = get_list_or_404(EnqCarReply,enq=enqobj)
    for a in rpobj:
        agrp=get_object_or_404(Agent,pk=a.agent.pk)
        agrp.pend-=1
        agrp.save()
    enqobj.delete()
    return HttpResponseRedirect(reverse('client:enqcarlist'))

@login_required
@client_required
def carrate(request,arch):
    registered=False
    if request.method=='POST':
        form =CarRating(request.POST)
        if form.is_valid():
            rate = form.cleaned_data['rating']
            a = get_object_or_404(EnqCarArchiv,pk=arch)
            a.rating = rate
            a.save()
            ag = get_object_or_404(Agent,pk=a.agent.pk)
            if ag.rating:
                ag.rating=(ag.rated*ag.rating+rate.stars)/(ag.rated+1)
                ag.rated+=1
            else:
                ag.rating=rate.stars
                ag.rated+=1
            ag.save()
            registered=True
    else:
        form = CarRating()
    return render(request,'client/carrate.html',{'form':form,'registered':registered,'rte':rate.stars})



@login_required
@client_required
def enqinsrnce(request):
    registered = False
    if request.method=='POST':
        enqinsrnceform = EnqInsrnceForm(data=request.POST)
        if enqinsrnceform.is_valid():
            enqinsrnce = enqinsrnceform.save(commit=False)
            enqinsrnce.client = get_object_or_404(Client,user=request.user)
            enqinsrnce.save()
            registered=True
        else:
            enqinsrnceform = EnqInsrnceForm()
    else:
        enqinsrnceform = EnqInsrnceForm()
    return render(request,'client/enqinsrnceform.html',{'enqinsrnceform':enqinsrnceform,'registered':registered,'insertme':'Client : '+str(request.user),'acc':'acc'})

@login_required
@client_required
def enqinsrncelist(request):
    list= [a for a in EnqInsrnce.objects.all() if a.client == get_object_or_404(Client,user=request.user)]
    return render(request,'client/enqinsrncelist.html',{'list':list,'insertme':'Client : '+str(request.user),'acc':'acc'})

@login_required
@client_required
def clientinsrnceaccpt(request,enq,acpt):
    enqobj = get_object_or_404(EnqInsrnce,pk=enq)
    acptobj=get_object_or_404(EnqInsrnceReply,pk=acpt)
    insrncearch = EnqInsrnceArchiv(client=enqobj.client,
                                    country=enqobj.country,
                                    type_of_insurance=enqobj.type_of_insurance,
                                    number_of_people=enqobj.number_of_people,
                                    travel_start_location=enqobj.travel_start_location,
                                    destination=enqobj.destination,
                                    additional_information=enqobj.additional_information,
                                    created=enqobj.created,
                                    agent=acptobj.agent,
                                    insurance_coverage=acptobj.insurance_coverage,
                                    charges=acptobj.charges,
                                    additional_information_reply=acptobj.additional_information,
                                    replied=acptobj.replied)
    agrt=get_object_or_404(Agent,pk=acptobj.agent.pk)
    agrt.pend-=1
    agrt.complete_insrnce+=1
    agrt.complete_all+=1
    agrt.save()
    insrncearch.save()
    enqobj.delete()
    return HttpResponseRedirect(reverse('client:enqinsrncelist'))

@login_required
@client_required
def enqinsrncedone(request):
    dlist=[a for a in EnqInsrnceArchiv.objects.all() if a.client == get_object_or_404(Client,user=request.user)]
    return render(request,'client/enqinsrncearch.html',{'dlist':dlist,'insertme':'Client : '+str(request.user),'acc':'acc'})

@login_required
@client_required
def enqinsrncedel(request,key):
    enqobj = get_object_or_404(EnqInsrnce,pk=key)
    rpobj = get_list_or_404(EnqInsrnceReply,enq=enqobj)
    for a in rpobj:
        agrp=get_object_or_404(Agent,pk=a.agent.pk)
        agrp.pend-=1
        agrp.save()
    enqobj.delete()
    return HttpResponseRedirect(reverse('client:enqinsrncelist'))

@login_required
@client_required
def insrncerate(request,arch):
    registered=False
    if request.method=='POST':
        form =InsrnceRating(request.POST)
        if form.is_valid():
            rate = form.cleaned_data['rating']
            a = get_object_or_404(EnqInsrnceArchiv,pk=arch)
            a.rating = rate
            a.save()
            ag = get_object_or_404(Agent,pk=a.agent.pk)
            if ag.rating:
                ag.rating=(ag.rated*ag.rating+rate.stars)/(ag.rated+1)
                ag.rated+=1
            else:
                ag.rating=rate.stars
                ag.rated+=1
            ag.save()
            registered=True
    else:
        form = InsrnceRating()
    return render(request,'client/insrncerate.html',{'form':form,'registered':registered,'rte':rate.stars})
