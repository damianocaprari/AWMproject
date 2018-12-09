from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #return HttpResponse("Storefront Hello World")
    context = {}
    #return render(request, 'storefront/base.html', context)
    return render(request, 'storefront/override_base.html', context)