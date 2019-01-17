from . import views
from django.urls import path


app_name = 'spells'

urlpatterns = [
    path('', views.index, name='index'),
]
