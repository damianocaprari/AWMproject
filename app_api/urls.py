from . import views
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

app_name = 'api'

router = routers.DefaultRouter()
router.register('characterclasses', views.CharacterClassView)
router.register('spells', views.SpellView)
router.register('users', views.UserView)
router.register('conditions', views.ConditionsView)

# router.register('users-detail', views.UserView)

urlpatterns = [
    # path('', views.api_root),
    # path('classes/', views.CharacterClassList.as_view(), name='characterclass-list'),
    # path('classes/<int:pk>/', views.CharacterClassDetail.as_view(), name='characterclass-detail'),
    # path('users/', views.UserList.as_view(), name='user-list'),
    # path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    # path('spells/', views.SpellList.as_view(), name='spell-list'),
    # path('spells/<int:pk>/', views.SpellDetail.as_view(), name='spell-detail'),
    path('', include(router.urls)),
]

#urlpatterns = format_suffix_patterns(urlpatterns)

