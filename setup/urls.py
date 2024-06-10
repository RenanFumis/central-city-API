
from django.contrib import admin
from django.urls import path
from central_city.views import index, herois, viloes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('herois/', herois),
    path('viloes/', viloes),

]
