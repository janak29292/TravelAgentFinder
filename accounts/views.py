from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from accounts.decorators import client_required, agent_required, staff_required
from accounts.models import Agent, Client
from accounts.forms import ChangeName, ChangeEmail, ChangePhone, ChangeDateofBirth, ChangeAddress, ChangeOccupation, ChangeCompany
from client.models import (EnqAir, EnqBus, EnqCar, EnqHotel, EnqInsrnce, EnqTour, EnqTrain, EnqVisa,
                            EnqAirArchiv, EnqBusArchiv, EnqCarArchiv, EnqHotelArchiv, EnqInsrnceArchiv, EnqTourArchiv, EnqTourArchiv, EnqVisaArchiv)
from gly.models import PMessage

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                if user.is_client:
                    return HttpResponseRedirect(reverse('accounts:userprofile'))
                elif user.is_superuser:
                    return HttpResponseRedirect(reverse('admin:index'))
                elif user.is_staff:
                    return HttpResponseRedirect(reverse('accounts:userprofile'))
            else:
                # If account is not active:
                return render(request, 'login.html', {'error':'Login Failed: Account Inactive'})
        else:
            # print("Someone tried to login and failed.")
            # print("They used username: {} and password: {}".format(username,password))
            return render(request, 'login.html', {'error':'Login Failed: Incorrect Credentials'})

    else:
        return render(request, 'login.html', {})


@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))

@login_required
def userprofile(request):
    return render(request,'profile.html',{'insertme':'Hello '+ request.user.username})



@login_required
def editpassword(request):
    updated=False
    if request.method=='POST':
        updateform=PasswordChangeForm(request.user, request.POST)
        if updateform.is_valid():
            user = updateform.save()
            update_session_auth_hash(request, user)  # Important!
        else:
            updateform=PasswordChangeForm(request.user)
    else:
        updateform=PasswordChangeForm(request.user)
    return render(request,'profileform.html',{'updateform':updateform,'updated':updated,'insertme':'Edit Password'})

@login_required
@client_required
def editname(request):
    updated=False
    if request.method =='POST':
        updateform=ChangeName(request.POST)
        if updateform.is_valid():
            first_name=updateform.cleaned_data['first_name']
            last_name=updateform.cleaned_data['last_name']
            a = get_object_or_404(Client,user=request.user)
            a.first_name=first_name
            a.last_name=last_name
            a.save()
            updated=True
        else:
            updateform=ChangeName()
    else:
        updateform=ChangeName()
    return render(request,'profileform.html',{'updateform':updateform,'updated':updated,'insertme':'Edit Name'})

@login_required
def editemail(request):
    updated=False
    if request.method =='POST':
        updateform=ChangeEmail(request.POST)
        if updateform.is_valid():
            email=updateform.cleaned_data['email']
            a = request.user
            a.email=email
            a.save()
            updated=True
        else:
            updateform=ChangeEmail()
    else:
        updateform=ChangeEmail()
    return render(request,'profileform.html',{'updateform':updateform,'updated':updated,'insertme':'Update Email'})

@login_required
@client_required
def editphone(request):
    updated=False
    if request.method =='POST':
        updateform=ChangePhone(request.POST)
        if updateform.is_valid():
            phone=updateform.cleaned_data['phone']
            a = get_object_or_404(Client,user=request.user)
            a.phone=phone
            a.save()
            updated=True
        else:
            updateform=ChangePhone()
    else:
        updateform=ChangePhone()
    return render(request,'profileform.html',{'updateform':updateform,'updated':updated,'insertme':'Update Phone'})


@login_required
@client_required
def editdob(request):
    updated=False
    if request.method =='POST':
        updateform=ChangeDateofBirth(request.POST)
        if updateform.is_valid():
            date_of_birth=updateform.cleaned_data['date_of_birth']
            a = get_object_or_404(Client,user=request.user)
            a.date_of_birth=date_of_birth
            a.save()
            updated=True
        else:
            updateform=ChangeDateofBirth()
    else:
        updateform=ChangeDateofBirth()
    return render(request,'profileform.html',{'updateform':updateform,'updated':updated,'insertme':'Edit Date of Birth'})


@login_required
@client_required
def editaddress(request):
    updated=False
    if request.method =='POST':
        updateform=ChangeAddress(request.POST)
        if updateform.is_valid():
            address=updateform.cleaned_data['address']
            a = get_object_or_404(Client,user=request.user)
            a.address=address
            a.save()
            updated=True
        else:
            updateform=ChangeAddress()
    else:
        updateform=ChangeAddress()
    return render(request,'profileform.html',{'updateform':updateform,'updated':updated,'insertme':'Update Address'})


@login_required
@client_required
def editocc(request):
    updated=False
    if request.method =='POST':
        updateform=ChangeOccupation(request.POST)
        if updateform.is_valid():
            occupation=updateform.cleaned_data['occupation']
            a = get_object_or_404(Client,user=request.user)
            a.occupation=occupation
            a.save()
            updated=True
        else:
            updateform=ChangeOccupation()
    else:
        updateform=ChangeOccupation()
    return render(request,'profileform.html',{'updateform':updateform,'updated':updated,'insertme':'Update Occupation'})

@login_required
@agent_required
def editcompany(request):
    updated=False
    if request.method =='POST':
        updateform=ChangeCompany(request.POST)
        if updateform.is_valid():
            company_name=updateform.cleaned_data['company_name']
            a = get_object_or_404(Agent,user=get_object_or_404(Client,user=request.user))
            a.company_name=company_name
            a.save()
            updated=True
        else:
            updateform=ChangeCompany()
    else:
        updateform=ChangeCompany()
    return render(request,'profileform.html',{'updateform':updateform,'updated':updated,'insertme':'Update Company Name'})



@login_required
@staff_required
def admintourlist(request):
    list= [a for a in EnqTour.objects.all()]
    return render(request,'admin/admintourlist.html',{'list':list,'acc':'acc'})

@login_required
@staff_required
def adminhotellist(request):
    list= [a for a in EnqHotel.objects.all()]
    return render(request,'admin/adminhotellist.html',{'list':list,'acc':'acc'})

@login_required
@staff_required
def admintrainlist(request):
    list= [a for a in EnqTrain.objects.all()]
    return render(request,'admin/admintrainlist.html',{'list':list,'acc':'acc'})

@login_required
@staff_required
def adminairlist(request):
    list= [a for a in EnqAir.objects.all()]
    return render(request,'admin/adminairlist.html',{'list':list,'acc':'acc'})

@login_required
@staff_required
def adminbuslist(request):
    list= [a for a in EnqBus.objects.all()]
    return render(request,'admin/adminbuslist.html',{'list':list,'acc':'acc'})

@login_required
@staff_required
def adminvisalist(request):
    list= [a for a in EnqVisa.objects.all()]
    return render(request,'admin/adminvisalist.html',{'list':list,'acc':'acc'})

@login_required
@staff_required
def admincarlist(request):
    list= [a for a in EnqCar.objects.all()]
    return render(request,'admin/admincarlist.html',{'list':list,'acc':'acc'})

@login_required
@staff_required
def admininsrncelist(request):
    list= [a for a in EnqInsrnce.objects.all()]
    return render(request,'admin/admininsrncelist.html',{'list':list,'acc':'acc'})


@login_required
@staff_required
def admintourdone(request):
    adlist=[a for a in EnqTourArchiv.objects.all()]
    return render(request,'admin/admintourdone.html',{'adlist':adlist,'acc':'acc'})

@login_required
@staff_required
def adminhoteldone(request):
    adlist=[a for a in EnqHotelArchiv.objects.all()]
    return render(request,'admin/adminhoteldone.html',{'adlist':adlist,'acc':'acc'})

@login_required
@staff_required
def admintraindone(request):
    adlist=[a for a in EnqTrainArchiv.objects.all()]
    return render(request,'admin/admintraindone.html',{'adlist':adlist,'acc':'acc'})

@login_required
@staff_required
def adminairdone(request):
    adlist=[a for a in EnqAirArchiv.objects.all()]
    return render(request,'admin/adminairdone.html',{'adlist':adlist,'acc':'acc'})

@login_required
@staff_required
def adminbusdone(request):
    adlist=[a for a in EnqBusArchiv.objects.all()]
    return render(request,'admin/adminbusdone.html',{'adlist':adlist,'acc':'acc'})

@login_required
@staff_required
def adminvisadone(request):
    adlist=[a for a in EnqVisaArchiv.objects.all()]
    return render(request,'admin/adminvisadone.html',{'adlist':adlist,'acc':'acc'})

@login_required
@staff_required
def admincardone(request):
    adlist=[a for a in EnqCarArchiv.objects.all()]
    return render(request,'admin/admincardone.html',{'adlist':adlist,'acc':'acc'})

@login_required
@staff_required
def admininsrncedone(request):
    adlist=[a for a in EnqInsrnceArchiv.objects.all()]
    return render(request,'admin/admininsrncedone.html',{'adlist':adlist,'acc':'acc'})

@login_required
@staff_required
def listofclients(request):
    loc=[a for a in Client.objects.all() if a.user.is_agent!=True ]
    return render(request,'listofclients.html',{'loc':loc,'acc':'acc','insertme':'List of Clients'})

@login_required
@staff_required
def listofagents(request):
    loa=[a for a in Agent.objects.all()]
    return render(request,'listofagents.html',{'loa':loa,'acc':'acc','insertme':'List of Agents'})

@login_required
@staff_required
def contactmsgs(request):
    msgs =[a for a in PMessage.objects.all()]
    return render(request,'contactmsgs.html',{'msgs':msgs,'acc':'acc','insertme':'Contact Us Messages'})
