from django.core.management.base import BaseCommand
import openpyxl
from dash.models import Emprestimos

class Command(BaseCommand):
    help = "Import data from an Excel file into the database"

    def handle(self, *args, **kwargs):
        file_path = "/Users/tiagomendonca/Downloads/planilha_final_3.xlsx"
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active

        for row in sheet.iter_rows(min_row=2, values_only=True):  
            Emprestimos.objects.create(
                nome=row[0],
                matricula=row[1],
                cpf=row[2],
                status_solicitacao=row[3],
                valor_solicitado=row[4],
                valor_total_ccb=row[5],
                quantidade_parcelas=row[6],
                valor_parcela=row[7],
                data_primeiro_vencimento=row[8],
                data_assinatura=row[9],
                cet_mes=row[10],
                unidades=row[11],
                cnpj=row[12],
                status_operacao=row[13],
                parcelas_pagas=row[14],
                parcelas_remanescentes=row[15],
                saldo_devedor=row[16],
                data_demissao=row[17],
                ultimo_pagamento=row[18],
                identificador_operacao=row[19],
            )


