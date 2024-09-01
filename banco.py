# Importa a classe List do módulo typing para permitir a definição de listas tipadas.
# Importa a função sleep do módulo time para pausar a execução do programa por um tempo determinado.
# Importa as classes Cliente e Conta do módulo models.cliente e models.conta, respectivamente.

from typing import List
from time import sleep
from models.cliente import Cliente
from models.conta import Conta

# Cria uma lista global para armazenar as contas criadas.
contas: List[Conta] = []

# Função principal do programa que chama o menu principal.
def main() -> None:
    menu()

# Função que exibe o menu principal e captura a opção escolhida pelo usuário.
def menu() -> None:
    print('=====================================')
    print('============== ATM ==================')
    print('=========== LF Bank ===============')
    print('=====================================')

    print('Selecione uma opção no menu: ')
    print('1 - Criar conta')
    print('2 - Efetuar saque')
    print('3 - Efetuar depósito')
    print('4 - Efetuar transferência')
    print('5 - Listar contas')
    print('6 - Sair do sistema')

    # Captura a opção escolhida pelo usuário.
    opcao: int = int(input())

    # Verifica a opção escolhida e chama a função correspondente.
    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        # Encerra o programa.
        print('Volte sempre')
        sleep(2)
        exit(0)
    else:
        # Informa ao usuário que a opção é inválida e exibe o menu novamente.
        print('Opção inválida')
        sleep(2)
        menu()

# Função para criar uma nova conta bancária.
def criar_conta() -> None:
    print('Informe os dados do cliente: ')

    # Captura as informações do cliente.
    nome: str = input('Nome do cliente: ')
    email: str = input('E-mail do cliente: ')
    cpf: str = input('CPF do cliente: ')
    data_nascimento: str = input('Data de nascimento do cliente: ')

    # Cria um objeto Cliente com as informações fornecidas.
    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)

    # Cria uma nova conta para o cliente.
    conta: Conta = Conta(cliente)

    # Adiciona a nova conta à lista global de contas.
    contas.append(conta)

    print('Conta criada com sucesso.')
    print('Dados da conta: ')
    print('-----------------')
    print(conta)
    sleep(2)
    # Retorna ao menu principal.
    menu()

# Função para realizar um saque em uma conta.
def efetuar_saque() -> None:
    # Verifica se existem contas cadastradas.
    if len(contas) > 0:
        numero: int = int(input('Informe o número da sua conta: '))

        # Busca a conta pelo número informado.
        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor do saque: '))

            # Realiza o saque.
            conta.sacar(valor)
        else:
            print(f'Não foi encontrada a conta com número {numero}')
    else:
        print('Ainda não existem contas cadastradas.')
    sleep(2)
    menu()

# Função para realizar um depósito em uma conta.
def efetuar_deposito() -> None:
    # Verifica se existem contas cadastradas.
    if len(contas) > 0:
        numero: int = int(input('Informe o número da sua conta: '))

        # Busca a conta pelo número informado.
        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor do depósito: '))

            # Realiza o depósito.
            conta.depositar(valor)
        else:
            print(f'Não foi encontrada uma conta com número {numero}')
    else:
        print('Ainda não existem contas cadastradas.')
    sleep(2)
    menu()

# Função para realizar uma transferência entre contas.
def efetuar_transferencia() -> None:
    # Verifica se existem contas cadastradas.
    if len(contas) > 0:
        numero_o: int = int(input('Informe o número da sua conta: '))

        # Busca a conta de origem pelo número informado.
        conta_o: Conta = buscar_conta_por_numero(numero_o)

        if conta_o:
            numero_d: int = int(input('Informe o número da conta destino: '))

            # Busca a conta de destino pelo número informado.
            conta_d: Conta = buscar_conta_por_numero(numero_d)

            if conta_d:
                valor: float = float(input('Informe o valor da transferência: '))

                # Realiza a transferência.
                conta_o.transferir(conta_d, valor)
            else:
                print(f'A conta destino com número {numero_d} não foi encontrada.')
        else:
            print(f'A sua conta com número {numero_o} não foi encontrada.')
    else:
        print('Ainda não existem contas cadastradas.')
    sleep(2)
    menu()

# Função para listar todas as contas cadastradas.
def listar_contas() -> None:
    # Verifica se existem contas cadastradas.
    if len(contas) > 0:
        print('Listagem de contas')

        # Exibe as informações de cada conta.
        for conta in contas:
            print(conta)
            print('--------------------')
            sleep(1)
    else:
        print('Não existem contas cadastradas.')
    sleep(2)
    menu()

# Função para buscar uma conta pelo número.
def buscar_conta_por_numero(numero: int) -> Conta:
    c: Conta = None

    # Verifica se existem contas cadastradas.
    if len(contas) > 0:
        # Procura a conta correspondente ao número informado.
        for conta in contas:
            if conta.numero == numero:
                c = conta
    return c

# Verifica se o script está sendo executado diretamente e, se sim, chama a função principal.
if __name__ == '__main__':
    main()
