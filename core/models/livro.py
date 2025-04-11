from django.db import models


class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    isbn = models.CharField(max_length=32, null=True, blank=True)
    quantidade = models.IntegerField(default=0, null=True, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2,default=0, null=True, blank=True)
    

    def __str__(self):
        return f"({self.id}) - {self.titulo} - ({self.quantidade})"