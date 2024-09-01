# Importa as classes date e datetime do módulo datetime para manipulação de datas.

from datetime import date
from datetime import datetime

# Função que converte uma data do tipo date para uma string formatada no padrão brasileiro (dia/mês/ano).
def date_para_str(data: date) -> str:
    return data.strftime('%d/%m/%Y')

# Função que converte uma string formatada no padrão brasileiro (dia/mês/ano) para uma data do tipo date.
def str_para_date(data: str) -> date:
    return datetime.strptime(data, '%d/%m/%Y')

# Função que formata um valor float para uma string no formato de moeda brasileira (R$ 0.000,00).
def formata_float_str_moeda(valor: float) -> str:
    return f'R$ {valor:,.2f}'
