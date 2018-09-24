from django.shortcuts import render,get_object_or_404
from gly.models import Destinat, PMessage
# Create your views here.

def index(request):
    return render(request,'index.html',{'home':True})

def destination(request, place_key):
    post = get_object_or_404(Destinat, name=place_key)
    return render(request,'destinations.html',{'place':post})

def plans(request):
    return render(request,'membership_plans.html',{'insertme':'Membership Plans'})

def agentbenefits(request):
    return render(request,'agents_benefits.html',{'insertme':'Agent Benefits'})

def clientbenefits(request):
    return render(request,'cust_benefits.html',{'insertme':'Client Benefits'})

def about(request):
    return render(request,'about_us.html',{'insertme':'About Us'})

def contact(request):
    posted=False
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        messobj = PMessage(name=name,email=email,subject=subject,message=message)
        messobj.save()
        posted=True
    return render(request,'contact_us.html',{'insertme':'Contact Us','posted':posted})
