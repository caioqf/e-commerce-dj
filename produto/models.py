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
    imagem_produto = models.ImageField(upload_to=None, height_field=None, width_field=None, default='didi.jpg')


    def __str__(self):
        return self.nome