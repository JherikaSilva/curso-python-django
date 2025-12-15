from rest_framework import serializers
from .models import Tarefa
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class TarefaSerializer(serializers.ModelSerializer):
    """
    Serializer para o Model Tarefa.
    Responsabilidades:
    1. Converter Tarefa → JSON (serialização)
    2. Converter JSON → Tarefa (desserialização)
    3. Validar dados de entrada
    
    """
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Tarefa
        fields = ['id','user', 'titulo', 'concluida', 'criada_em']
        read_only_fields = ['id','user', 'criada_em']


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Adicionar campos customizados ao payload
        token['username'] = user.username
        token['email'] = user.email
        token['is_staff'] = user.is_staff
        return token        
        
        
    