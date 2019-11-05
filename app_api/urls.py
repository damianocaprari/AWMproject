from app_api import views  # TODO le view vanno importate dalle varie app
from app_characterclasses.views import CharacterClassViewSet
from app_conditions.views import ConditionViewSet
from app_profiles.views import ProfileViewSet, UserViewSet
from app_spells.views import SpellViewSet, SpellTagViewSet, SpellAdditionalInfoViewSet
from app_monsters.views import MonsterViewSet
from django.urls import path, include
from rest_framework import routers


app_name = 'api'

router = routers.DefaultRouter()
router.register('characterclasses', CharacterClassViewSet)
router.register('conditions', ConditionViewSet)
router.register('profiles', ProfileViewSet)
router.register('spells', SpellViewSet)
router.register('spell_additional_info', SpellAdditionalInfoViewSet)
router.register('spelltags', SpellTagViewSet)
router.register('users', UserViewSet)
router.register('monsters', MonsterViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
