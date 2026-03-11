class Conta():
    def __init__(self, id, nome, saldo=0):
        self.nome = nome
        self._id = id
        self._saldo = saldo
        self._historico = []

    def ver_saldo(self):
        return self._saldo
    
    def depositar(self, valor_monetario):
        self._saldo += valor_monetario 
        transação = {"Valor Atual": self._saldo, "valor depositado": valor_monetario}
        self._historico.append(transação)
        return self._saldo
        
    def sacar(self, valor_retirado):
        if self._saldo > 0 and self._saldo >= valor_retirado:
            self._saldo -= valor_retirado
            transação = {"Valor Atual": self._saldo, "valor retirado": valor_retirado}
            self._historico.append(transação)
            return self._saldo