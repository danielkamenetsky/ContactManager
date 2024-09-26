from django.urls import path
from . import views

#  Maps specific URL paths ot the views. Defines how users access different parts of the application.

urlpatterns = [
    path('', views.home, name='home'), 
     path('contact_list/', views.contact_list, name='contact_list'), # URL for the contact list
    # You can add more URL patterns here for other views related to contacts
]
