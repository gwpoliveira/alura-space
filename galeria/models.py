from django.db import models
from datetime import datetime
class Fotografia(models.Model):
    OPCOES_CATEGORIAS = [
        ("Nebulosa", "Nebulosa"),
        ("Estrela", "Estrela"),
        ("GALÁXIA", "Galáxia"),
        ("PLANETA", "Planeta")
    ]
    nome = models.CharField(max_length=100, null=False, blank=False)
    legeda = models.CharField(max_length=200, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIAS, default="")
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    publicado = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
         return self.nome
