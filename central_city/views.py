from rest_framework import viewsets, filters
from central_city.models import Heroi, Vilao
from central_city.serializer import HeroiSerializer, VilaoSerializer
from django_filters.rest_framework import DjangoFilterBackend

class HeroisViewSet(viewsets.ModelViewSet):
    '''Exibiondo todos os herois'''
    queryset = Heroi.objects.all()
    serializer_class = HeroiSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['nome', 'primeira_aparicao']

class ViloesViewSet(viewsets.ModelViewSet):
    '''Exibindo todos os viloes'''
    queryset = Vilao.objects.all()
    serializer_class = VilaoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['nome', 'primeira_aparicao']