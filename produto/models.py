from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    # Para representar o nome do objeto no django admin
    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)
    modelo = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    preco = models.FloatField(max_length=255)
    avaliacao = models.IntegerField()

    def __str__(self):
        return self.nome