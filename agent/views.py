from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from agent.forms import UserForm, ClientForm, AgentForm, EnqTourReplyForm, EnqHotelReplyForm, EnqTrainReplyForm, EnqAirReplyForm, EnqBusReplyForm, EnqVisaReplyForm, EnqCarReplyForm, EnqInsrnceReplyForm
from accounts.decorators import agent_required
from accounts.models import Agent, Client
from client.models import EnqTour, EnqHotel, EnqTrain, EnqAir, EnqBus, EnqVisa, EnqCar, EnqInsrnce, EnqTourArchiv, EnqHotelArchiv, EnqTrainArchiv, EnqAirArchiv, EnqBusArchiv, EnqVisaArchiv, EnqCarArchiv, EnqInsrnceArchiv

# Create your views here.
# @login_required
# @agent_required
# def agentdash(request):
#     enqhotelno= len([a for a in EnqHotel.objects.all() if a.client != request.user])
#     return render(request,'agent/dashboard.html',{'insertme':'My Account','enqhotelno':enqhotelno})

def agentsignup(request):
    er=''
    registered = False

    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)
        client_form=ClientForm(data=request.POST)
        agent_form = AgentForm(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid() and client_form.is_valid() and agent_form.is_valid():

            # Save User Form to Database
            user = user_form.save(commit=False)
            user.is_agent = True
            user.is_client = True

            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            user.save()

            # Now we deal with the extra info!
            client = client_form.save(commit=False)
            client.user = user
            client.save()
            # Can't commit yet because we still need to manipulate
            agent = agent_form.save(commit=False)
            agent.user =client
            agent.save()
            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            # raise agent_form.errors
            user_form=UserForm()
            client_form=ClientForm()
            agent_form = AgentForm()
            er = 'Registration Failed'

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form=UserForm()
        client_form=ClientForm()
        agent_form = AgentForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'agent/signup.html',
                          {'user_form':user_form,
                           'client_form':client_form,
                           'agent_form':agent_form,
                           'registered':registered,
                           'insertme':'Agent SignUp',
                           'er':er})

@login_required
@agent_required
def agenttourlist(request):
    clist =[a for a in EnqTour.objects.all() if a.client != get_object_or_404(Client,user=request.user)]
    return render(request,'agent/agenttourlist.html',{'clist':clist,'insertme':'Agent : '+str(request.user),'acc':'acc'})

@login_required
@agent_required
def agenttourrply(request,key):
    replied= False
    if request.method =='POST':
        enqtourreplyform = EnqTourReplyForm(data=request.POST)
        if enqtourreplyform.is_valid():
            enqtourreply = enqtourreplyform.save(commit=False)
            enqtourreply.enq = get_object_or_404(EnqTour,pk=key)
            enqtourreply.agent = get_object_or_404(Agent,user=get_object_or_404(Client,user=request.user))
            agt=get_object_or_404(Agent,pk=enqtourreply.agent.pk)
            agt.pend+=1
            agt.save()
            enqtourreply.save()
            replied=True
        else:
            enqtourreplyform = EnqTourReplyForm()
    else:
        enqtourreplyform = EnqTourReplyForm()
    return render(request,'agent/agenttourrply.html',{'enqtourreplyform':enqtourreplyform,'replied':replied,'insertme':'Agent : '+str(request.user),'acc':'acc'})

@login_required
@agent_required
def agenttourpending(request):
    rlist =[a for a in EnqTour.objects.all()]
    return render(request,'agent/agenttourpend.html',{'rlist':rlist,'insertme':'Agent : '+str(request.user),'acc':'acc'})

@login_required
@agent_required
def agenttourdone(request):
    adlist=[a for a in EnqTourArchiv.objects.all() if a.agent == get_object_or_404(Agent,user=get_object_or_404(Client,user=request.user))]
    return render(request,'agent/agenttourdone.html',{'adlist':adlist,'insertme':'Agent : '+str(request.user),'acc':'acc'})

@login_required
@agent_required
def agenthotellist(request):
    clist =[a for a in EnqHotel.objects.all() if a.client != get_object_or_404(Client,user=request.user)]
    return render(request,'agent/agenthotellist.html',{'clist':clist,'insertme':'Agent : '+str(request.user),'acc':'acc'})

@login_required
@agent_required
def agenthotelrply(request,key):
    replied= False
    if request.method =='POST':
        enqhotelreplyform = EnqHotelReplyForm(data=request.POST)
        if enqhotelreplyform.is_valid():
            enqhotelreply = enqhotelreplyform.save(commit=False)
            enqhotelreply.enq = get_object_or_404(EnqHotel,pk=key)
            enqhotelreply.agent = get_object_or_404(Agent,user=get_object_or_404(Client,user=request.user))
            agt=get_object_or_404(Agent,pk=enqhotelreply.agent.pk)
            agt.pend+=1
            agt.save()
            enqhotelreply.save()
            replied=True
        else:
            enqhotelreplyform = EnqHotelReplyForm()
    else:
        enqhotelreplyform = EnqHotelReplyForm()
    return render(request,'agent/agenthotelrply.html',{'enqhotelreplyform':enqhotelreplyform,'replied':replied,'insertme':'Agent : '+str(request.user),'acc':'acc'})

@login_required
@agent_required
def agenthotelpending(request):
    rlist =[a for a in EnqHotel.objects.all()]
    return render(request,'agent/agenthotelpend.html',{'rlist':rlist,'insertme':'Agent : '+str(request.user),'acc':'acc'})

@login_required
@agent_required
def agenthoteldone(request):
    adlist=[a for a in EnqHotelArchiv.objects.all() if a.agent == get_object_or_404(Agent,user=get_object_or_404(Client,user=request.user))]
    return render(request,'agent/agenthoteldone.html',{'adlist':adlist,'insertme':'Agent : '+str(request.user),'acc':'acc'})


@login_required
@agent_required
def agenttrainlist(request):
    clist =[a for a in EnqTrain.objects.all() if a.client != get_object_or_404(Client,user=request.user)]
    return render(request,'agent/agenttrainlist.html',{'clist':clist,'insertme':'Agent : '+str(request.user),'acc':'acc'})

@login_required
@agent_required
def agenttrainrply(request,key):
    replied= False
    if request.method =='POST':
        enqtrainreplyform = EnqTrainReplyForm(data=request.POST)
        if enqtrainreplyform.is_valid():
            enqtrainreply = enqtrainreplyform.save(commit=False)
            enqtrainreply.enq = get_object_or_404(EnqTrain,pk=key)
            enqtrainreply.agent = get_object_or_404(Agent,user=get_object_or_404(Client,user=request.user))
            agt=get_object_or_404(Agent,pk=enqtrainreply.agent.pk)
            agt.pend+=1
            agt.save()
            enqtrainreply.save()
            replied=True
        else:
            enqtrainreplyform = EnqTrainReplyForm()
    else:
        enqtrainreplyform = EnqTrainReplyForm()
    return render(request,'agent/agenttrainrply.html',{'enqtrainreplyform':enqtrainreplyform,'replied':replied,'insertme':'Agent : '+str(request.user),'acc':'acc'})

@login_required
@agent_required
def agenttrainpending(request):
    rlist =[a for a in EnqTrain.objects.all()]
    return render(request,'agent/agenttrainpend.html',{'rlist':rlist,'insertme':'Agent : '+str(request.user),'acc':'acc'})

@login_required
@agent_required
def agenttraindone(request):
    adlist=[a for a in EnqTrainArchiv.objects.all() if a.agent == get_object_or_404(Agent,user=get_object_or_404(Client,user=request.user))]
    return render(request,'agent/agenttraindone.html',{'adlist':adlist,'insertme':'Agent : '+str(request.user),'acc':'acc'})


@login_required
@agent_required
def agentairlist(request):
    clist =[a for a in EnqAir.objects.all() if a.client != get_object_or_404(Client,user=request.user)]
    return render(request,'agent/agentairlist.html',{'clist':clist,'insertme':'Agent : '+str(request.user),'acc':'acc'})

@login_required
@agent_required
def agentairrply(request,key):
    replied= False
    if request.method =='POST':
        enqairreplyform = EnqAirReplyForm(data=request.POST)
        if enqairreplyform.is_valid():
            enqairreply = enqairreplyform.save(commit=False)
            enqairreply.enq = get_object_or_404(EnqAir,pk=key)
            enqairreply.agent = get_object_or_404(Agent,user=get_object_or_404(Client,user=request.user))
            agt=get_object_or_404(Agent,pk=enqairreply.agent.pk)
            agt.pend+=1
            agt.save()
            enqairreply.save()
            replied=True
        else:
            enqairreplyform = EnqAirReplyForm()
    else:
        enqairreplyform = EnqAirReplyForm()
    return render(request,'agent/agentairrply.html',{'enqairreplyform':enqairreplyform,'replied':replied,'insertme':'Agent : '+str(request.user),'acc':'acc'})

@login_required
@agent_required
def agentairpending(request):
    rlist =[a for a in EnqAir.objects.all()]
    return render(request,'agent/agentairpend.html',{'rlist':rlist,'insertme':'Agent : '+str(request.user),'acc':'acc'})

@login_required
@agent_required
def agentairdone(request):
    adlist=[a for a in EnqAirArchiv.objects.all() if a.agent == get_object_or_404(Agent,user=get_object_or_404(Client,user=request.user))]
    return render(request,'agent/agentairdone.html',{'adlist':adlist,'insertme':'Agent : '+str(request.user),'acc':'acc'})


@login_required
@agent_required
def agentbuslist(request):
    clist =[a for a in EnqBus.objects.all() if a.client != get_object_or_404(Client,user=request.user)]
    return render(request,'agent/agentbuslist.html',{'clist':clist,'insertme':'Agent : '+str(request.user),'acc':'acc'})

@login_required
@agent_required
def agentbusrply(request,key):
    replied= False
    if request.method =='POST':
        enqbusreplyform = EnqBusReplyForm(data=request.POST)
        if enqbusreplyform.is_valid():
            enqbusreply = enqbusreplyform.save(commit=False)
            enqbusreply.enq = get_object_or_404(EnqBus,pk=key)
            enqbusreply.agent = get_object_or_404(Agent,user=get_object_or_404(Client,user=request.user))
            agt=get_object_or_404(Agent,pk=enqbusreply.agent.pk)
            agt.pend+=1
            agt.save()
            enqbusreply.save()
            replied=True
        else:
            enqbusreplyform = EnqBusReplyForm()
    else:
        enqbusreplyform = EnqBusReplyForm()
    return render(request,'agent/agentbusrply.html',{'enqbusreplyform':enqbusreplyform,'replied':replied,'insertme':'Agent : '+str(request.user),'acc':'acc'})

@login_required
@agent_required
def agentbuspending(request):
    rlist =[a for a in EnqBus.objects.all()]
    return render(request,'agent/agentbuspend.html',{'rlist':rlist,'insertme':'Agent : '+str(request.user),'acc':'acc'})

@login_required
@agent_required
def agentbusdone(request):
    adlist=[a for a in EnqBusArchiv.objects.all() if a.agent == get_object_or_404(Agent,user=get_object_or_404(Client,user=request.user))]
    return render(request,'agent/agentbusdone.html',{'adlist':adlist,'insertme':'Agent : '+str(request.user),'acc':'acc'})


@login_required
@agent_required
def agentvisalist(request):
    clist =[a for a in EnqVisa.objects.all() if a.client != get_object_or_404(Client,user=request.user)]
    return render(request,'agent/agentvisalist.html',{'clist':clist,'insertme':'Agent : '+str(request.user),'acc':'acc'})

@login_required
@agent_required
def agentvisarply(request,key):
    replied= False
    if request.method =='POST':
        enqvisareplyform = EnqVisaReplyForm(data=request.POST)
        if enqvisareplyform.is_valid():
            enqvisareply = enqvisareplyform.save(commit=False)
            enqvisareply.enq = get_object_or_404(EnqVisa,pk=key)
            enqvisareply.agent = get_object_or_404(Agent,user=get_object_or_404(Client,user=request.user))
            agt=get_object_or_404(Agent,pk=enqvisareply.agent.pk)
            agt.pend+=1
            agt.save()
            enqvisareply.save()
            replied=True
        else:
            enqvisareplyform = EnqVisaReplyForm()
    else:
        enqvisareplyform = EnqVisaReplyForm()
    return render(request,'agent/agentvisarply.html',{'enqvisareplyform':enqvisareplyform,'replied':replied,'insertme':'Agent : '+str(request.user),'acc':'acc'})

@login_required
@agent_required
def agentvisapending(request):
    rlist =[a for a in EnqVisa.objects.all()]
    return render(request,'agent/agentvisapend.html',{'rlist':rlist,'insertme':'Agent : '+str(request.user),'acc':'acc'})

@login_required
@agent_required
def agentvisadone(request):
    adlist=[a for a in EnqVisaArchiv.objects.all() if a.agent == get_object_or_404(Agent,user=get_object_or_404(Client,user=request.user))]
    return render(request,'agent/agentvisadone.html',{'adlist':adlist,'insertme':'Agent : '+str(request.user),'acc':'acc'})


@login_required
@agent_required
def agentcarlist(request):
    clist =[a for a in EnqCar.objects.all() if a.client != get_object_or_404(Client,user=request.user)]
    return render(request,'agent/agentcarlist.html',{'clist':clist,'insertme':'Agent : '+str(request.user),'acc':'acc'})

@login_required
@agent_required
def agentcarrply(request,key):
    replied= False
    if request.method =='POST':
        enqcarreplyform = EnqCarReplyForm(data=request.POST)
        if enqcarreplyform.is_valid():
            enqcarreply = enqcarreplyform.save(commit=False)
            enqcarreply.enq = get_object_or_404(EnqCar,pk=key)
            enqcarreply.agent = get_object_or_404(Agent,user=get_object_or_404(Client,user=request.user))
            agt=get_object_or_404(Agent,pk=enqcarreply.agent.pk)
            agt.pend+=1
            agt.save()
            enqcarreply.save()
            replied=True
        else:
            enqcarreplyform = EnqCarReplyForm()
    else:
        enqcarreplyform = EnqCarReplyForm()
    return render(request,'agent/agentcarrply.html',{'enqcarreplyform':enqcarreplyform,'replied':replied,'insertme':'Agent : '+str(request.user),'acc':'acc'})

@login_required
@agent_required
def agentcarpending(request):
    rlist =[a for a in EnqCar.objects.all()]
    return render(request,'agent/agentcarpend.html',{'rlist':rlist,'insertme':'Agent : '+str(request.user),'acc':'acc'})

@login_required
@agent_required
def agentcardone(request):
    adlist=[a for a in EnqCarArchiv.objects.all() if a.agent == get_object_or_404(Agent,user=get_object_or_404(Client,user=request.user))]
    return render(request,'agent/agentcardone.html',{'adlist':adlist,'insertme':'Agent : '+str(request.user),'acc':'acc'})


@login_required
@agent_required
def agentinsrncelist(request):
    clist =[a for a in EnqInsrnce.objects.all() if a.client != get_object_or_404(Client,user=request.user)]
    return render(request,'agent/agentinsrncelist.html',{'clist':clist,'insertme':'Agent : '+str(request.user),'acc':'acc'})

@login_required
@agent_required
def agentinsrncerply(request,key):
    replied= False
    if request.method =='POST':
        enqinsrncereplyform = EnqInsrnceReplyForm(data=request.POST)
        if enqinsrncereplyform.is_valid():
            enqinsrncereply = enqinsrncereplyform.save(commit=False)
            enqinsrncereply.enq = get_object_or_404(EnqInsrnce,pk=key)
            enqinsrncereply.agent = get_object_or_404(Agent,user=get_object_or_404(Client,user=request.user))
            agt=get_object_or_404(Agent,pk=enqinsrncereply.agent.pk)
            agt.pend+=1
            agt.save()
            enqinsrncereply.save()
            replied=True
        else:
            enqinsrncereplyform = EnqInsrnceReplyForm()
    else:
        enqinsrncereplyform = EnqInsrnceReplyForm()
    return render(request,'agent/agentinsrncerply.html',{'enqinsrncereplyform':enqinsrncereplyform,'replied':replied,'insertme':'Agent : '+str(request.user),'acc':'acc'})

@login_required
@agent_required
def agentinsrncepending(request):
    rlist =[a for a in EnqInsrnce.objects.all()]
    return render(request,'agent/agentinsrncepend.html',{'rlist':rlist,'insertme':'Agent : '+str(request.user),'acc':'acc'})

@login_required
@agent_required
def agentinsrncedone(request):
    adlist=[a for a in EnqInsrnceArchiv.objects.all() if a.agent == get_object_or_404(Agent,user=get_object_or_404(Client,user=request.user))]
    return render(request,'agent/agentinsrncedone.html',{'adlist':adlist,'insertme':'Agent : '+str(request.user),'acc':'acc'})
