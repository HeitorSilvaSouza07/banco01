'''Está parte do projeto é responsavel por construir os atriubutos e metodos da classe cliente(conta)'''

class Conta():
    def __init__(self, id, nome, saldo=0):
        self._id = id
        self._nome = nome
        self._saldo = saldo
        self._historico = []

    #É uma propriedade da classe eresponsavel pela chadama dos atritutos da propria, nesse caso id do cliente( facilita a chamado do atributo)
    @property
    def id(self):
        return self._id

    #Retorna o nome
    @property
    def nome(self):
        return self._nome
    
    #ve o saldo em conta
    def ver_saldo(self):
        return self._saldo
    
    #metodo da classe, depositar dinheiro na conta
    def depositar(self, valor_monetario):
        self._saldo += valor_monetario 
        transacao = {"Valor Atual": self._saldo, "valor depositado": valor_monetario}
        self._historico.append(transacao)
        return self._saldo

    #metodo da classe,  retirar/ sacar dinheiro
    def sacar(self, valor_retirado):
        if self._saldo > 0 and self._saldo >= valor_retirado:
            self._saldo -= valor_retirado
            transacao = {f"valor retirado: {valor_retirado}"}
            self._historico.append(transacao)
            return True
        
        return False
    
    #lista historico de transaçoes
    def listar_historico(self):
        return self._historico
