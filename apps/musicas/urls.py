from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'musicas'

router = routers.DefaultRouter()
router.register('musicas', views.MusicaViewSet, basename='musicas')

urlpatterns = [
    path('', include(router.urls) )
]