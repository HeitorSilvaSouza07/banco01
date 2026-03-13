from conta import Conta

class Banco():
    def __init__(self):
        self._contas = []


    def criar_conta(self, id, nome):
        conta = Conta(id, nome)
        self._contas.append(conta)
        return conta
        
    def buscar_conta(self, id):
        for conta in self._contas:
            if conta.id == id:
                return conta
        return None
    
    def deletar_usuario(self, id):
        for conta in self._contas:
            if conta.id == id:
                self._contas.remove(conta)
                return True
        return False
    