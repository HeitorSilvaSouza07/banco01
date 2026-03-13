'''responsavel por uniar as validacoes e emteados das classes pára funcionamento do sistema bnacario da melhor forma possivel'''
from fastapi import FastAPI
from app.models.services.banco import Banco

#delcara app como fast api
app = FastAPI()

#criação do banco para gestão dos usuarios
banco = Banco()

#faz a criação da conta, metodo ja existente no banco e retorna se foi bem sucedido
@app.post("/criarconta")
def criar_conta(id: int, nome: str ):
    conta = banco.criar_conta( id, nome)
    return {"Mensagem": f"Conta criada para {conta.nome}"}

#depositar dinheiro na conta, para isso é feita a validação da conta e ai sim autorizada a transação
@app.post("/depositar")
def depositar(id: int, valor: float):
    conta = banco.buscar_conta(id)

    if conta is None:
        return {"erro": "Conta não encontrada"}

    saldo = conta.depositar(valor)
    return {"saldo": saldo}

#validação, saca dinheiro e 
@app.post("/sacar_dinheiro")
def sacar(id: int, valor: float):
    conta =  banco.buscar_conta(id)

    if not conta:
        return{"Usuario não encontrado"}
    
    saque =  conta.sacar(valor)

    if not saque:
        return {"valor invalido"}
    
    return{"Transação bem sucedida"}

#usa a validação se for retornado o nome da conta é printado que a conta existe se não é devolvido que a conta não existe
@app.get("/buscarconta")
def buscar_conta(id: int):
    conta = banco.buscar_conta(id)

    if conta is None:
        return {"erro": "Conta não encontrada"}

    return {
        "nome": conta.nome,
        "saldo": conta.ver_saldo()
    }

#por enquanto tentativa de listar historico
@app.get("/listar_historico")
def listas_historico(id: int):

    conta =  banco.buscar_conta(id)

    if not conta:
        return{"valor invalido"}
    
    historico = conta.listar_historico()
    return historico

#deleta a conta do usuario mas antes é feita a validação da existencia da conta 
@app.delete("/deletar_usuario")
def deletar(id: int):
    deletado = banco.deletar_usuario(id)

    if not deletado:
        return {"Usuario não deletado"}
    
    return{"Usuaurio deltado com sucesso"}