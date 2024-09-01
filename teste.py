from models.cliente import Cliente
from models.conta import Conta

# criando contas testes
messi: Cliente = Cliente('Lionel Messi', 'messi@gmail.com', '123.456.789-01', '24/06/1987')
batman: Cliente = Cliente('Batman', 'batman@gmail.com', '987.654.321-01', '01/05/1939')

# print(messi)
# print(angelina)

contaf: Conta = Conta(messi)
contaa: Conta = Conta(batman)

# print(contaf)
# print(contaa)

