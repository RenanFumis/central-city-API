
from django.contrib import admin
from django.urls import path, include
from central_city.views import HeroisViewSet, ViloesViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('herois', HeroisViewSet, basename='Herois')
router.register('viloes', ViloesViewSet, basename='Viloes')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

]
