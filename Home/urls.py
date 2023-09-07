from re import A
from django.urls import path 
from . import views as v

urlpatterns = [
    path('' , v.HomeView , name="HomeView"),
    path('about/' , v.aboutview , name="aboutview"),
    # path('contact/' , v.ContactUsView.as_view() , name="contactview"),
    path('contact/' , v.contactview , name="contactview"),
    path('questions/' , v.faq , name='faq'),
    path('coming-soon/' , v.coming , name='com'),
    path('H404/' , v.h404 , name='H404'),
    path('privacy-policy/' , v.privacy , name='privacy'),
    path('workwithus/' , v.privacy , name='workwithus'),
]
