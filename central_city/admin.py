from django.contrib import admin
from central_city.models import Heroi, Vilao

class HeroiAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codinome', 'poder', 'profissao', 'primeira_aparicao')
    list_display_links = ('nome', 'codinome')
    search_fields = ('nome', 'codinome', 'primeira_aparicao')
    list_per_page = 20

admin.site.register(Heroi, HeroiAdmin)

class VilaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codinome', 'poder', 'profissao', 'primeira_aparicao')
    list_display_links = ('nome', 'codinome')
    search_fields = ('nome', 'codinome', 'primeira_aparicao')
    list_per_page = 20

admin.site.register(Vilao, VilaoAdmin)



