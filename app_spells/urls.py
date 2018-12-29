from django.urls import path
from . import views


app_name = 'spells'

urlpatterns = [
    path('', views.index, name='index'),
]

