class Conta:
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        self.saldo = 0 
        self.historico = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.append(f"Depósito: R$ {valor}")
            print(f"Depósito de R$ {valor} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")
    
    def sacar(self, valor):
        if valor <= 0 :
            print("Valor inválido para saque.")
        elif valor > self.saldo:
            print("Saldo insuficiente para saque.")
        else:
            self.saldo -= valor 
            self.historico.append(f"Saque: R$ {valor}")
            print(f"Saque de R$ {valor} realizado com sucesso.")

    def ver_saldo(self):
        print(f"Saldo atual: R$ {self.saldo}")

    def ver_historico(self):
        print("\n=== Historico ===")
        for transacao in self.historico:
            print(transacao)
