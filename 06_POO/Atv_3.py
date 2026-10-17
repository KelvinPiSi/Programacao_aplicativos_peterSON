import time


class ContaBancaria:
    def __init__(self,titular, saldo_inicial = 0):
        self.titular = titular
        self.saldo_inicial = saldo_inicial

    def depositar(self, deposito):
        print(f"Depositando {deposito} reais em conta")
        self.saldo_inicial += deposito
        print(f'O saldo agora é {self.saldo_inicial}')
    def sacar(self,saque):
        print("Iniciando processo de saque...")
        time.sleep(3)
        if self.saldo_inicial < saque :
            print("Saldo Insuficiente para saque")
        else :
            print("Sacando dinheiro...")
            time.sleep(5)
            print("Saque concluido")
            self.saldo_inicial = self.saldo_inicial - saque
            print(f"Saldo atual agora é {self.saldo_inicial}")
    def extrato(self):
        print(f"\nTitular -- {self.titular}\nSaldo atual -- {self.saldo_inicial}")

Conta1 = ContaBancaria(titular="Pessoa1")
Conta2 = ContaBancaria(titular="Pessoa2", saldo_inicial=500)


Conta1.extrato()
Conta1.depositar(300)
Conta1.sacar(150)

Conta2.extrato()
Conta2.depositar(200)
Conta2.sacar(800)

