class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, quantia):
        self.saldo += quantia
        print(f"Depositado: {quantia}. Saldo atual: {self.saldo}")

    def sacar(self, quantia):
        if quantia <= self.saldo:
            self.saldo -= quantia
            print(f"Sacado: {quantia}. Saldo atual: {self.saldo}")
        else:
            print("Saldo insuficiente.")

    def verificar_saldo(self):
        print(f"Saldo atual: {self.saldo}")

conta = ContaBancaria("João", 1000)
conta.depositar(500)
conta.sacar(200)
conta.verificar_saldo()
