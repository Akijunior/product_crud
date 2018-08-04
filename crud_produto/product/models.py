from django.db import models

# Create your models here.
class User(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()

    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome

class Product(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(decimal_places=2, max_digits=5)
    quantidade = models.IntegerField(default=1)
