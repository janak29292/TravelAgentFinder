from django.conf.urls import url
from client import views

app_name='client'

urlpatterns=[
# url(r'^$',views.clientdash,name='clientdash'),
url(r'^SignUp/$',views.clientsignup,name='clientsignup'),
url(r'^TourEnquiry/$',views.enqtour,name='enqtour'),
url(r'^TourEnquiryList/$',views.enqtourlist,name='enqtourlist'),
url(r'^TourEnquiryFinished/$',views.enqtourdone,name='enqtourdone'),
url(r'^TourEnquiryDelete/(?P<key>[%&+ \w]+)/$',views.enqtourdel,name='enqtourdel'),
url(r'^AgentTourRating/(?P<arch>[%&+ \w]+)/$',views.tourrate,name='tourrate'),
url(r'^TourAccepted/(?P<enq>[%&+ \w]+)/(?P<acpt>[%&+ \w]+)/$',views.clienttouraccpt,name='clienttouraccpt'),
url(r'^HotelEnquiry/$',views.enqhotel,name='enqhotel'),
url(r'^HotelEnquiryList/$',views.enqhotellist,name='enqhotellist'),
url(r'^HotelEnquiryFinished/$',views.enqhoteldone,name='enqhoteldone'),
url(r'^HotelEnquiryDelete/(?P<key>[%&+ \w]+)/$',views.enqhoteldel,name='enqhoteldel'),
url(r'^AgentHotelRating/(?P<arch>[%&+ \w]+)/$',views.hotelrate,name='hotelrate'),
url(r'^HotelAccepted/(?P<enq>[%&+ \w]+)/(?P<acpt>[%&+ \w]+)/$',views.clienthotelaccpt,name='clienthotelaccpt'),
url(r'^TrainEnquiry/$',views.enqtrain,name='enqtrain'),
url(r'^TrainEnquiryList/$',views.enqtrainlist,name='enqtrainlist'),
url(r'^TrainEnquiryFinished/$',views.enqtraindone,name='enqtraindone'),
url(r'^TrainEnquiryDelete/(?P<key>[%&+ \w]+)/$',views.enqtraindel,name='enqtraindel'),
url(r'^AgentTrainRating/(?P<arch>[%&+ \w]+)/$',views.trainrate,name='trainrate'),
url(r'^TrainAccepted/(?P<enq>[%&+ \w]+)/(?P<acpt>[%&+ \w]+)/$',views.clienttrainaccpt,name='clienttrainaccpt'),
url(r'^FlightEnquiry/$',views.enqair,name='enqair'),
url(r'^FlightEnquiryList/$',views.enqairlist,name='enqairlist'),
url(r'^FlightEnquiryFinished/$',views.enqairdone,name='enqairdone'),
url(r'^FlightEnquiryDelete/(?P<key>[%&+ \w]+)/$',views.enqairdel,name='enqairdel'),
url(r'^AgentFlightRating/(?P<arch>[%&+ \w]+)/$',views.airrate,name='airrate'),
url(r'^FlightAccepted/(?P<enq>[%&+ \w]+)/(?P<acpt>[%&+ \w]+)/$',views.clientairaccpt,name='clientairaccpt'),
url(r'^BusEnquiry/$',views.enqbus,name='enqbus'),
url(r'^BusEnquiryList/$',views.enqbuslist,name='enqbuslist'),
url(r'^BusEnquiryFinished/$',views.enqbusdone,name='enqbusdone'),
url(r'^BusEnquiryDelete/(?P<key>[%&+ \w]+)/$',views.enqbusdel,name='enqbusdel'),
url(r'^AgentBusRating/(?P<arch>[%&+ \w]+)/$',views.busrate,name='busrate'),
url(r'^BusAccepted/(?P<enq>[%&+ \w]+)/(?P<acpt>[%&+ \w]+)/$',views.clientbusaccpt,name='clientbusaccpt'),
url(r'^VisaAndPassportEnquiry/$',views.enqvisa,name='enqvisa'),
url(r'^VisaAndPassportEnquiryList/$',views.enqvisalist,name='enqvisalist'),
url(r'^VisaAndPassportEnquiryFinished/$',views.enqvisadone,name='enqvisadone'),
url(r'^VisaAndPassportEnquiryDelete/(?P<key>[%&+ \w]+)/$',views.enqvisadel,name='enqvisadel'),
url(r'^AgentVisaAndPassportRating/(?P<arch>[%&+ \w]+)/$',views.visarate,name='visarate'),
url(r'^VisaAndPassportAccepted/(?P<enq>[%&+ \w]+)/(?P<acpt>[%&+ \w]+)/$',views.clientvisaaccpt,name='clientvisaaccpt'),
url(r'^RentalCarEnquiry/$',views.enqcar,name='enqcar'),
url(r'^RentalCarEnquiryList/$',views.enqcarlist,name='enqcarlist'),
url(r'^RentalCarEnquiryFinished/$',views.enqcardone,name='enqcardone'),
url(r'^RentalCarEnquiryDelete/(?P<key>[%&+ \w]+)/$',views.enqcardel,name='enqcardel'),
url(r'^AgentRentalCarRating/(?P<arch>[%&+ \w]+)/$',views.carrate,name='carrate'),
url(r'^RentalCarAccepted/(?P<enq>[%&+ \w]+)/(?P<acpt>[%&+ \w]+)/$',views.clientcaraccpt,name='clientcaraccpt'),
url(r'^TravelInsuranceEnquiry/$',views.enqinsrnce,name='enqinsrnce'),
url(r'^TravelInsuranceEnquiryList/$',views.enqinsrncelist,name='enqinsrncelist'),
url(r'^TravelInsuranceEnquiryFinished/$',views.enqinsrncedone,name='enqinsrncedone'),
url(r'^TravelInsuranceEnquiryDelete/(?P<key>[%&+ \w]+)/$',views.enqinsrncedel,name='enqinsrncedel'),
url(r'^AgentTravelInsuranceRating/(?P<arch>[%&+ \w]+)/$',views.insrncerate,name='insrncerate'),
url(r'^TravelInsuranceAccepted/(?P<enq>[%&+ \w]+)/(?P<acpt>[%&+ \w]+)/$',views.clientinsrnceaccpt,name='clientinsrnceaccpt'),
]
