from django.db import models

class Heroi(models.Model):
    nome = models.CharField(blank=False, null=False, max_length=100)
    codinome = models.CharField(blank=False, max_length=100)
    poder = models.CharField(max_length=700)
    profissao = models.CharField(max_length=200)
    primeira_aparicao = models.CharField(blank=False, max_length=200)

    def __str__(self):
        return self.nome

class Vilao(models.Model):
    nome = models.CharField(blank=False, max_length=100)
    codinome = models.CharField(blank=False, max_length=100)
    poder = models.CharField(max_length=700)
    profissao = models.CharField(max_length=200)
    primeira_aparicao = models.CharField(blank=False, max_length=200)

    def __str__(self):
        return self.nome