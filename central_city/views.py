from rest_framework import viewsets
from central_city.models import Heroi, Vilao
from central_city.serializer import HeroiSerializer, VilaoSerializer

class HeroisViewSet(viewsets.ModelViewSet):
    '''Exibiondo todos os herois'''
    queryset = Heroi.objects.all()
    serializer_class = HeroiSerializer

class ViloesViewSet(viewsets.ModelViewSet):
    '''Exibindo todos os viloes'''
    queryset = Vilao.objects.all()
    serializer_class = VilaoSerializer