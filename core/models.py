from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=120)
    descricao = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.nome

class Unidade(models.Model):
    nome = models.CharField(max_length=120)
    endereco = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.nome

class Sala(models.Model):
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE, related_name="salas")
    nome = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.unidade.nome} - {self.nome}"


class Status(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Status"

    def __str__(self):
        return self.nome


class Bem(models.Model):
    nome = models.CharField(max_length=200)
    tombo = models.CharField(max_length=50, unique=True)
    
    categoria = models.ForeignKey(
        'Categoria', on_delete=models.SET_NULL, null=True, blank=True
    )
    unidade = models.ForeignKey(Unidade, on_delete=models.PROTECT, related_name="bens")
    sala = models.ForeignKey(Sala, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True)
    
    valor_estimado = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Bem"
        verbose_name_plural = "Bens"

    def __str__(self):
        return f"{self.nome} ({self.tombo})"


