from django.db import models

class Unidade(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Unidade"
        verbose_name_plural = "Unidades"


class Sala(models.Model):
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome} - {self.unidade.nome}"

    class Meta:
        verbose_name = "Sala"
        verbose_name_plural = "Salas"


class Status(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Status"  # mesmo no plural, não muda


class Bem(models.Model):
    nome = models.CharField(max_length=100)
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Bem"
        verbose_name_plural = "Bens"
