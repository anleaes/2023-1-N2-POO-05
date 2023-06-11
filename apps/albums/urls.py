from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'albums'

router = routers.DefaultRouter()
router.register('albums', views.AlbumViewSet, basename='albums')

urlpatterns = [
    path('', include(router.urls) )
]