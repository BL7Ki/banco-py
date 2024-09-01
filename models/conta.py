# Importa a classe Cliente do módulo models.cliente.
# Importa a função formata_float_str_moeda do módulo utils.helper para formatar valores monetários.

from models.cliente import Cliente
from utils.helper import formata_float_str_moeda

# Define a classe Conta que representa uma conta bancária.
class Conta:

    # Atributo de classe que define um código inicial para o número das contas.
    codigo: int = 100

    # Método construtor que inicializa uma instância da classe Conta.
    def __init__(self: object, cliente: Cliente) -> None:
        # Atributo privado que armazena o número da conta, baseado no código estático da classe.
        self.__numero: int = Conta.codigo
        # Atributo privado que armazena o cliente associado a esta conta.
        self.__cliente: Cliente = cliente
        # Atributo privado que armazena o saldo da conta, inicialmente zero.
        self.__saldo: float = 0.0
        # Atributo privado que armazena o limite da conta, inicialmente 100.0.
        self.__limite: float = 100.0
        # Atributo privado que armazena o saldo total da conta, que é o saldo mais o limite.
        self.__saldo_total: float = self._calcula_saldo_total
        # Incrementa o código estático para o próximo número de conta.
        Conta.codigo += 1

    # Método especial que define como a instância da classe será representada como string.
    def __str__(self: object) -> str:
        return f'Número da conta: {self.numero} \nCliente: {self.cliente.nome} ' \
               f'\nSaldo Total: {formata_float_str_moeda(self.saldo_total)}'

    # Propriedade que retorna o número da conta.
    @property
    def numero(self: object) -> int:
        return self.__numero

    # Propriedade que retorna o cliente associado à conta.
    @property
    def cliente(self: object) -> Cliente:
        return self.__cliente

    # Propriedade que retorna o saldo da conta.
    @property
    def saldo(self: object) -> float:
        return self.__saldo

    # Setter para modificar o saldo da conta.
    @saldo.setter
    def saldo(self: object, valor: float) -> None:
        self.__saldo = valor

    # Propriedade que retorna o limite da conta.
    @property
    def limite(self: object) -> float:
        return self.__limite

    # Setter para modificar o limite da conta.
    @limite.setter
    def limite(self: object, valor: float) -> None:
        self.__limite = valor

    # Propriedade que retorna o saldo total da conta (saldo + limite).
    @property
    def saldo_total(self: object) -> float:
        return self.__saldo_total

    # Setter para modificar o saldo total da conta.
    @saldo_total.setter
    def saldo_total(self: object, valor: float) -> None:
        self.__saldo_total = valor

    # Propriedade que calcula e retorna o saldo total da conta.
    @property
    def _calcula_saldo_total(self: object) -> float:
        return self.saldo + self.limite

    # Método para realizar um depósito na conta.
    def depositar(self: object, valor: float) -> None:
        # Verifica se o valor do depósito é positivo.
        if valor > 0:
            # Adiciona o valor ao saldo da conta.
            self.saldo = self.saldo + valor
            # Atualiza o saldo total da conta.
            self.saldo_total = self._calcula_saldo_total
            print('Depósito efetuado com sucesso!')
        else:
            print('Erro ao efetuar depósito. Tente novamente')

    # Método para realizar um saque da conta.
    def sacar(self: object, valor: float) -> None:
        # Verifica se o valor do saque é positivo e não excede o saldo total da conta.
        if 0 < valor <= self.saldo_total:
            # Se o saldo é suficiente para o saque.
            if self.saldo >= valor:
                # Deduz o valor do saldo.
                self.saldo = self.saldo - valor
                # Atualiza o saldo total.
                self.saldo_total = self._calcula_saldo_total
            else:
                # Se o saldo não é suficiente, usa o limite da conta para cobrir a diferença.
                restante: float = self.saldo - valor
                self.limite = self.limite + restante
                self.saldo = 0
                self.saldo_total = self._calcula_saldo_total
            print('Saque efetuado com sucesso')
        else:
            print('Saque não realizado. Tente novamente')

    # Método para realizar uma transferência entre contas.
    def transferir(self: object, destino: object, valor: float) -> None:
        # Verifica se o valor da transferência é positivo e não excede o saldo total da conta.
        if valor > 0 and self.saldo_total >= valor:
            # Se o saldo é suficiente para a transferência.
            if self.saldo >= valor:
                # Deduz o valor do saldo da conta de origem.
                self.saldo = self.saldo - valor
                # Atualiza o saldo total da conta de origem.
                self.saldo_total = self._calcula_saldo_total
                # Adiciona o valor ao saldo da conta de destino.
                destino.saldo = destino.saldo + valor
                # Atualiza o saldo total da conta de destino.
                destino.saldo_total = destino._calcula_saldo_total
            else:
                # Se o saldo não é suficiente, usa o limite da conta de origem para cobrir a diferença.
                restante: float = self.saldo - valor
                self.saldo = 0
                self.limite = self.limite + restante
                self.saldo_total = self._calcula_saldo_total
                destino.saldo = destino.saldo + valor
                destino.saldo_total = destino._calcula_saldo_total
            print('Transferência realizada com sucesso.')
        else:
            print('Transferência não realizada. Tente novamente')
