
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConditionViewSet
from . import views


router = DefaultRouter()
router.register(r'conditions', ConditionViewSet)

urlpatterns = [
    path("", include(router.urls))
]




app_name = 'conditions'

#urlpatterns = [
#    path('', views.index, name='index'),
#]

