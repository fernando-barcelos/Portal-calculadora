from django.db import models


class Usuario(models.Model):
    idusuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(null=False, max_length=85)
    senha = models.CharField(max_length=15, null=False)
    dtinclusao = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'usuario'

    def __str__(self):
        return f"{self.nome} - {self.email} - {self.idusuario}"
