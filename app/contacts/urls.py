from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # URL for the contact list
    # You can add more URL patterns here for other views related to contacts
]
