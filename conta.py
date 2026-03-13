class Conta():
    def __init__(self, id, nome, saldo=0):
        self._id = id
        self._nome = nome
        self._saldo = saldo
        self._historico = []

    @property
    def id(self):
        return self._id

    @property
    def nome(self):
        return self._nome
    
    def ver_saldo(self):
        return self._saldo
    
    def depositar(self, valor_monetario):
        self._saldo += valor_monetario 
        transacao = {"Valor Atual": self._saldo, "valor depositado": valor_monetario}
        self._historico.append(transacao)
        return self._saldo
        
    def sacar(self, valor_retirado):
        if self._saldo > 0 and self._saldo >= valor_retirado:
            self._saldo -= valor_retirado
            transacao = {f"valor retirado: {valor_retirado}"}
            self._historico.append(transacao)
            return True
        
        return False
    
    def listar_historico(self):
        return self._historico
