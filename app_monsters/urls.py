from . import views
from django.urls import path


app_name = 'monsters'

urlpatterns = [
    path('', views.index, name='index'),
]
