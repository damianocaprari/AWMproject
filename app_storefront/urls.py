from django.urls import path, include
from . import views


app_name = 'storefront'

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('', include('django.contrib.auth.urls')),
]