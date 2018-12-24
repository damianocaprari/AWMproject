from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout as dj_logout
from django.contrib.auth.decorators import login_required

def index(request):
    #return HttpResponse("Storefront Hello World")
    context = {}
    return render(request, 'storefront/base.html', context)

"""
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username,
    password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
        else:
            # Return a 'disabled account' error message
            pass
    else:
    # Return an 'invalid login' error message.
        pass


def logout(request):
    dj_logout(request)
    # Redirect to a success page
    pass
"""