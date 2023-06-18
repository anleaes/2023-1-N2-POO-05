from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'comentarios'

router = routers.DefaultRouter()
router.register('comentarios', views.ComentarioViewSet, basename='comentarios')

urlpatterns = [
    path('', include(router.urls) )
]
