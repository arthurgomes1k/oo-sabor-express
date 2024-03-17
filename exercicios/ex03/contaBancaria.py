class ContaBancaria:

    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False  # Atributo protegido

    def __str__(self):
        return f"Conta de {self.titular} - Saldo: R${self.saldo}"
    
    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo
    
    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True

conta1 = ContaBancaria("João", 1000)
conta2 = ContaBancaria("Maria", 500)

conta3 = ContaBancaria("Carlos", 200)
print(f"Antes de ativar: Conta ativa? {conta3._ativo}")
ContaBancaria.ativar_conta(conta3)
print(f"Depois de ativar: Conta ativa? {conta3._ativo}")

conta4 = ContaBancaria("Fernanda", 1500)
print(f"Titular da conta 4: {conta4.titular}")

print(conta1)
print(conta2)