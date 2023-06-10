from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pessoas/', include('pessoas.urls', namespace='pessoas')),
    path('artistas/', include('artistas.urls', namespace='artistas')),
]
