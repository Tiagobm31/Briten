from django.db import models


class Emprestimos(models.Model):
    nome = models.CharField(max_length=255)  
    matricula = models.CharField(max_length=20) 
    cpf = models.CharField(max_length=11)
    status_solicitacao = models.CharField(max_length=50)
    valor_solicitado = models.DecimalField(max_digits=10, decimal_places=2) 
    valor_total_ccb = models.DecimalField(max_digits=10, decimal_places=2)  
    quantidade_parcelas = models.IntegerField()
    valor_parcela = models.DecimalField(max_digits=10, decimal_places=2)
    data_primeiro_vencimento = models.DateField()
    data_assinatura = models.DateField()
    cet_mes = models.DecimalField(max_digits=10, decimal_places=4)  
    unidades = models.CharField(max_length=255)  
    cnpj = models.CharField(max_length=18)  
    status_operacao = models.CharField(max_length=50)  
    parcelas_pagas = models.IntegerField()  
    parcelas_remanescentes = models.IntegerField()  
    saldo_devedor = models.DecimalField(max_digits=10, decimal_places=3)  
    data_demissao = models.DateField(null=True, blank=True)  
    ultimo_pagamento = models.DateField()  
    identificador_operacao = models.CharField(max_length=50)  

    def __str__(self):
        return self.nome 

