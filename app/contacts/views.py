from django.shortcuts import render

from django.http import HttpResponse


# Contains views (handlers for HTTP requests) which handle what happens when a user accesses different URLs (i.e. rendering a template, queryingthe database)
def home(request):
    return HttpResponse('<h1>Hello<h1>')

def contact_list(request):
    return HttpResponse('<h1>Bye<h1>')
