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
    
    def transição_entre_usuarios(self, id1, id2, valor):
    
        conta1 = self.buscar_conta(id1)
        conta2 = self.buscar_conta(id2)
        if conta1 is None or conta2 is None:
            return False
        else:
            for conta in self._contas:
                if conta.id == id1:
                     resultado = conta.sacar(valor)
                     if resultado is False:
                        return False
                
                if conta.id == id2:
                    conta.depositar(valor)
                    

            return True
        
        

