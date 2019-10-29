from . import views
from django.urls import path

from app_monsters import views
from django.urls import path, include
from rest_framework import routers

app_name = 'monsters'


#urlpatterns = [
#    path('', views.index, name='index'),
#]
