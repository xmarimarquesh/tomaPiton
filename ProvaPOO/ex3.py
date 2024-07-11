class Cliente:
    nome_cliente = ''
    numero_agencia = 0
    numero_conta = 0
    saldo_cliente = 0
    tipo_conta = ''
    contas = 0

    def __init__(self, nome_cliente, numero_agencia, numero_conta, saldo_cliente, tipo_conta):
        self.__nome_cliente = nome_cliente
        self.__numero_agencia = numero_agencia
        self.__numero_conta = numero_conta
        self.__saldo_cliente = saldo_cliente
        self.__tipo_conta = tipo_conta
    
    def getCliente(self):
        print(f'Cliente: {self.__nome_cliente} | Agencia: {self.__numero_agencia} | Conta: {self.__numero_conta} | Saldo: {self.__saldo_cliente} | Tipo de conta: {self.__tipo_conta}')
    
    def setCliente(self):
        #Exemplo 1 de 'setar' algo:
        self.__saldo_cliente = self.__saldo_cliente - 100
        print(f"Descontos de R$100,00 foram feitos.\nSaldo: {self.__saldo_cliente}")
        #Exemplo 2:
        self.__tipo_conta = 'Poupança'
        print(f'Conta alterada com sucesso!')
    
    
    @staticmethod
    def AbrirConta(contas):
        contas = contas + 1
        print(f'Neste banco há {contas} contas abertas')

mariana = Cliente('Mariana', 122143, 12312321423, 2000, 'Corrente')
mariana.setCliente()
mariana.getCliente()
mariana.AbrirConta(100)