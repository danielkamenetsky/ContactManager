from django.shortcuts import render

from django.http import HttpResponse


# Contains views (handlers for HTTP requests) which handle what happens when a user accesses different URLs (i.e. rendering a template, queryingthe database)
def home(request):
    return render(request, 'home.html')

def contact_list(request):
    return render(request, 'contact_list.html')
