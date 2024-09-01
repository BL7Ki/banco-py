# Importa a classe date do módulo datetime para manipulação de datas.
# Importa as funções date_para_str e str_para_date do módulo utils.helper para conversão de datas.

from datetime import date
from utils.helper import date_para_str, str_para_date

# Define a classe Cliente que representa um cliente de um sistema bancário.
class Cliente:
    # Atributo de classe que define um código inicial para identificar cada cliente.
    contador: int = 101

    # Método construtor que inicializa uma instância da classe Cliente.
    def __init__(self: object, nome: str, email: str, cpf: str, data_nascimento: str) -> None:
        # Atributo privado que armazena o código do cliente, baseado no contador estático da classe.
        self.__codigo: int = Cliente.contador
        # Atributo privado que armazena o nome do cliente.
        self.__nome: str = nome
        # Atributo privado que armazena o email do cliente.
        self.__email: str = email
        # Atributo privado que armazena o CPF do cliente.
        self.__cpf: str = cpf
        # Atributo privado que armazena a data de nascimento do cliente, convertida de string para date.
        self.__data_nascimento: date = str_para_date(data_nascimento)
        # Atributo privado que armazena a data de cadastro do cliente, definida como a data atual.
        self.__data_cadastro: date = date.today()
        # Incrementa o contador estático para o próximo código de cliente.
        Cliente.contador += 1

    # Propriedade que retorna o código do cliente.
    @property
    def codigo(self: object) -> int:
        return self.__codigo

    # Propriedade que retorna o nome do cliente.
    @property
    def nome(self: object) -> str:
        return self.__nome

    # Propriedade que retorna o email do cliente.
    @property
    def email(self: object) -> str:
        return self.__email

    # Propriedade que retorna o CPF do cliente.
    @property
    def cpf(self: object) -> str:
        return self.__cpf

    # Propriedade que retorna a data de nascimento do cliente formatada como string.
    @property
    def data_nascimento(self: object) -> str:
        return date_para_str(self.__data_nascimento)

    # Propriedade que retorna a data de cadastro do cliente formatada como string.
    @property
    def data_cadastro(self: object) -> str:
        return date_para_str(self.__data_cadastro)

    # Método especial que define como a instância da classe será representada como string.
    def __str__(self: object) -> str:
        return f'Código: {self.codigo} \nNome: {self.nome} \nData de Nascimento: {self.data_nascimento} ' \
               f'\nCadastro: {self.data_cadastro}'
