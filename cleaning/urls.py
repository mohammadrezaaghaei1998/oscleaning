from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('about-us', views.about_us, name='about-us'), 
    path('services', views.services, name='services'), 
    path('portfolio', views.portfolio, name='portfolio'),
     path('contact-us', views.contact, name='contact-us'),


    



    
]