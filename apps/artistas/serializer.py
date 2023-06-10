from .models import Artistas
from rest_framework import serializers

class ArtistasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artistas
        fields = '__all__'
        
        # Para chamar todos os atributos:
        # fields = '__all__'
        
        # Para chamar somentes os atributos de interesse:
        # fields = ['id','created_on', 'updated_on', 'name', 'description']