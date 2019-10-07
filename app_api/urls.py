from app_api import views  # TODO le view vanno importate dalle varie app
from app_spells.views import SpellViewSet, SpellTagViewSet
from app_conditions.views import ConditionViewSet
from django.urls import path, include
from rest_framework import routers


app_name = 'api'

router = routers.DefaultRouter()
router.register('characterclasses', views.CharacterClassView)
router.register('spells', SpellViewSet)
router.register('spelltags', SpellTagViewSet)
router.register('users', views.UserView)
router.register('conditions', ConditionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


