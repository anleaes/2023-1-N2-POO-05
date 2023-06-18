from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('albums/', include('albums.urls', namespace='albums')),
    path('musicas/', include('musicas.urls', namespace='musicas')),
    path('artistas/', include('artistas.urls', namespace='artistas')),
    path('usuarios/', include('usuarios.urls', namespace='usuarios')),
]
