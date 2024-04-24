# Sistemabancario te, que ter: titular, cpf, numero da conta, saldo, tipo de conta
# tem que fazer: saque, deposito, transferencia, tirar extrato

class Conta():

    def __init__(self, titular, cpf, tipo_conta, num_conta, saldo=0):
        self.titular = titular
        self.cpf = cpf
        self.tipo_conta = tipo_conta
        self.num_conta = num_conta
        self.saldo = saldo
        self.extrato = []

    def deposito(self, valor, ):
        if valor>0:
            self.saldo+= valor
            # igual a self.saldo=self.saldo + valor
            saida = 'Deposito feito na conta no valor de: ' +str(valor)
            self.extrato.append(saida)
        else:
            print('Valor inválido')

    def saque(self, valor):
        if valor<=0:
            print('Valor inválido')
        elif self.saldo >= valor:
            self.saldo -= valor
            saida = 'Saque de: ' +str(valor)
            self.extrato.append(saida)
        else:
            print('Valor do saque maior que o saldo ;-;')

    def transferencia(self, destino, valor):
        if valor >0 and self.saldo >= valor:
            destino.saldo += valor
            self.saque(valor)
            saida = 'Transferencia de: ' +str(valor) + 'para conta de: ' + destino.titular
            self.extrato.append(saida)
        else:
            print('Valor inválido ou saldo insuficíente')

    def verificar_extrato(self):
        print('Extrato')
        for item in self.extrato:
            print(item)


conta1 = Conta('Dio Brando', '8456486488898', 'corrente', '05587-2' )
conta2 = Conta('Caroline', '747897646465', 'corrente', '08784-9')
print(conta1.titular)

conta1.deposito(200)
print(conta1.saldo)

conta1.saque(152.66)
print(conta1.saldo)

conta1.transferencia(conta2, 5.3)
print('c1', conta1.saldo)
print('c2', conta2.saldo)

