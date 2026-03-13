'''classe de serviços de gerenciamento da classe conta'''
from app.models.conta import Conta

#no caso de um sistema bancariom um banco
class Banco():
    def __init__(self):
        self._contas = []

    #cria conta atraves do metodo classe
    def criar_conta(self, id, nome):
        conta = Conta(id, nome)
        self._contas.append(conta)
        return conta
        
    #validação da existencia da conta no sistema 
    def buscar_conta(self, id):
        for conta in self._contas:
            if conta.id == id:
                return conta
        return None
    
    #deleta usuario
    def deletar_usuario(self, id):
        for conta in self._contas:
            if conta.id == id:
                self._contas.remove(conta)
                return True
        return False
    