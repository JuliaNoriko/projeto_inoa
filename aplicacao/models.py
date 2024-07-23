from django.db import models

class Ativo(models.Model):
    simbolo = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.simbolo

class ParametroAtivo(models.Model):
    ativo = models.ForeignKey(Ativo, on_delete=models.CASCADE)
    limite_inferior = models.DecimalField(max_digits=10, decimal_places=2)
    limite_superior = models.DecimalField(max_digits=10, decimal_places=2)
    periodicidade = models.IntegerField(help_text="Periodicidade em minutos")

    def __str__(self):
        return f'{self.ativo.simbolo} - {self.limite_inferior} - {self.limite_superior}'

class Cotacao(models.Model):
    ativo = models.ForeignKey(Ativo, on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.ativo.simbolo} - {self.preco} - {self.data_hora}'
