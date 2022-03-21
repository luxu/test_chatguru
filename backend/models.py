from django.db import models


class Planeta(models.Model):
    nome = models.CharField(
        max_length=30
    )
    clima = models.CharField(
        max_length=20
    )
    diametro = models.IntegerField()
    populacao = models.IntegerField()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Planeta'
        verbose_name_plural = 'Planetas'
        ordering = ['-pk']


class Filme(models.Model):
    nome = models.CharField(
        max_length=100
    )
    data_lancamento = models.DateTimeField(
        null=True
    )
    planetas = models.ForeignKey(
        Planeta,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Filme'
        verbose_name_plural = 'Filmes'
        ordering = ['-pk']
