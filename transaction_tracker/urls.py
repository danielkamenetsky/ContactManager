from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

# This file routes HTTP requests to the appropriate views, which then return templates or handle form submissions.
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.home, name='home'), 
    path('', include('transactions.urls')), 
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

]