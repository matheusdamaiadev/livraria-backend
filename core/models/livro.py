from django.db import models


class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    isbn = models.CharField(max_length=32, null=True, blank=True)
    quantidade = models.IntegerField(null=True, blank=True, default=0)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)

    def __str__(self):
        return f'({self.id}) {self.titulo} ({self.quantidade})'
