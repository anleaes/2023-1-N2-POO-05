
from django.urls import include, path
from rest_framework import routers

from . import views

app_name = 'usuarios'

router = routers.DefaultRouter()
router.register('usuarios', views.UserViewSet, basename='usuarios')

urlpatterns = [
    path('', include(router.urls))
]