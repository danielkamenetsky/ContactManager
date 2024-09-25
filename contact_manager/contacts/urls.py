from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_list, name='contact_list'),  # URL for the contact list
    # You can add more URL patterns here for other views related to contacts
]
