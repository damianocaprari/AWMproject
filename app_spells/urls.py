from django.urls import path, include
from . import views


app_name = 'spells'

urlpatterns = [
    path('', views.index, name='index'),
]