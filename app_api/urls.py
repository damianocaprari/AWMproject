from app_api import views  # TODO le view vanno importate dalle varie app
from app_spells.views import SpellView, SpellTagView
from django.urls import path, include
from rest_framework import routers


app_name = 'api'

router = routers.DefaultRouter()
router.register('characterclasses', views.CharacterClassView)
router.register('spells', SpellView)
router.register('spelltags', SpellTagView)
router.register('users', views.UserView)
router.register('conditions', views.ConditionsView)

urlpatterns = [
    path('', include(router.urls)),
]


