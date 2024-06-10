import re
from rest_framework import serializers
from .models import Heroi, Vilao

class HeroiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heroi
        fields = ['id', 'nome', 'codinome', 'poder', 'profissao', 'primeira_aparicao']

    def validate_nome(self, nome):
        pattern = r"^[A-Za-zÀ-ÖØ-öø-ÿ'\"\s]+$"

        if not re.match(pattern, nome):
            raise serializers.ValidationError('Nome deve conter apenas letras')
        
        return nome

class VilaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vilao
        fields = ['id', 'nome', 'codinome', 'poder', 'profissao', 'primeira_aparicao']

    def validate_nome(self, nome):
        pattern = r"^[A-Za-zÀ-ÖØ-öø-ÿ'\"\s]+$"

        if not re.match(pattern, nome):
            raise serializers.ValidationError('Nome deve conter apenas letras')
        
        return nome