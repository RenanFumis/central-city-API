import re
from rest_framework import serializers
from .models import Heroi, Vilao
from .validators import *

class HeroiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heroi
        fields = ['id', 'nome', 'codinome', 'poder', 'profissao', 'primeira_aparicao', 'origem']

    def validate(self, data):
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':'O nome do herói deve conter apenas letras'})
        return data

class VilaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vilao
        fields = ['id', 'nome', 'codinome', 'poder', 'profissao', 'primeira_aparicao', 'origem']

    def validate(self, data):
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':'O nome do vilão deve conter apenas letras'})
        return data