from django.db import models
from apps.login.models import Usuario

class Operacao(models.Model):
    idoperacao = models.AutoField(primary_key=True)
    idusuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    parametros = models.CharField( null=False)
    resultado = models.CharField(null=False)
    dtinclusao = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'operacao'

    def __str__(self):
        return f"Operação {self.idoperacao} - Usuário: {self.idusuario.nome} - Resultado: {self.resultado}"