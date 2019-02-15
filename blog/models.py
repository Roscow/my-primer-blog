from django.db import models
from django.utils import timezone




class Entrada(models.Model):
    autor = models.ForeignKey('auth.user',on_delete=models.CASCADE )
    titulo = models.CharField(max_length=150)
    fecha = models.DateField(default=timezone.now())
    categoria = models.CharField(max_length=150)
    texto = models.TextField()

    def __str__():
        return titulo+ ', '+ autor



