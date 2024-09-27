from django.urls import path
from . import views

#  Maps specific URL paths ot the views. Defines how users access different parts of the application.

urlpatterns = [
    path('', views.home, name='home'), 
    path('transaction_list/', views.transaction_list, name='transaction_list'),
    path('add_transaction/', views.add_transaction, name='add_transaction'),
    path('<str:transaction_id>/', views.transaction_detail, name='transaction_detail'),


    # You can add more URL patterns here for other views related to
]
