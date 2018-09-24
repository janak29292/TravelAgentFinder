from django.conf.urls import url
from accounts import views

app_name = 'accounts'

urlpatterns=[
    url(r'^login/$',views.user_login,name='user_login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^Profile/$',views.userprofile,name='userprofile'),
    url(r'^Messages/$',views.contactmsgs,name='contactmsgs'),
    url(r'^ListofAgents/$',views.listofagents,name='listofagents'),
    url(r'^ListofClients/$',views.listofclients,name='listofclients'),
    url(r'^Profile/ChangePassword/$',views.editpassword,name='editpassword'),
    url(r'^Profile/ChangeName/$',views.editname,name='editname'),
    url(r'^Profile/ChangeEmail/$',views.editemail,name='editemail'),
    url(r'^Profile/ChangePhone/$',views.editphone,name='editphone'),
    url(r'^Profile/ChangeDateofBirth/$',views.editdob,name='editdob'),
    url(r'^Profile/ChangeAddress/$',views.editaddress,name='editaddress'),
    url(r'^Profile/ChangeOccupation/$',views.editocc,name='editocc'),
    url(r'^Profile/ChangeCompany/$',views.editcompany,name='editcompany'),
    url(r'^TourEnquiryList/$',views.admintourlist,name='admintourlist'),
    url(r'^HotelEnquiryList/$',views.adminhotellist,name='adminhotellist'),
    url(r'^TrainEnquiryList/$',views.admintrainlist,name='admintrainlist'),
    url(r'^FlightEnquiryList/$',views.adminairlist,name='adminairlist'),
    url(r'^BusEnquiryList/$',views.adminbuslist,name='adminbuslist'),
    url(r'^VisaAndPassportEnquiryList/$',views.adminvisalist,name='adminvisalist'),
    url(r'^RentalCarEnquiryList/$',views.admincarlist,name='admincarlist'),
    url(r'^TravelInsuranceEnquiryList/$',views.admininsrncelist,name='admininsrncelist'),
    url(r'^TourComplete/$',views.admintourdone,name='admintourdone'),
    url(r'^HotelComplete/$',views.adminhoteldone,name='adminhoteldone'),
    url(r'^TrainComplete/$',views.admintraindone,name='admintraindone'),
    url(r'^FlightComplete/$',views.adminairdone,name='adminairdone'),
    url(r'^BusComplete/$',views.adminbusdone,name='adminbusdone'),
    url(r'^VisaAndPassportComplete/$',views.adminvisadone,name='adminvisadone'),
    url(r'^RentalCarComplete/$',views.admincardone,name='admincardone'),
    url(r'^TravelInsuranceComplete/$',views.admininsrncedone,name='admininsrncedone'),
]
