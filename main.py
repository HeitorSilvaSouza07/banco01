from fastapi import FastAPI
from banco import Banco

app = FastAPI()

banco = Banco()

@app.post("/criarconta")
def criar_conta(id: int, nome: str ):
    conta = banco.criar_conta( id, nome)
    return {"Mensagem": f"Conta criada para {conta.nome}"}


@app.post("/depositar")
def depositar(id: int, valor: float):
    conta = banco.buscar_conta(id)

    if conta is None:
        return {"erro": "Conta não encontrada"}

    saldo = conta.depositar(valor)
    return {"saldo": saldo}

@app.post("/sacar_dinheiro")
def sacar(id: int, valor: float):
    conta =  banco.buscar_conta(id)

    if not conta:
        return{"Usuario não encontrado"}
    
    saque =  conta.sacar(valor)

    if not saque:
        return {"valor invalido"}
    
    return{"Transação bem sucedida"}

@app.get("/buscarconta")
def buscar_conta(id: int):
    conta = banco.buscar_conta(id)

    if conta is None:
        return {"erro": "Conta não encontrada"}

    return {
        "nome": conta.nome,
        "saldo": conta.ver_saldo()
    }

@app.get("/listar_historico")
def listas_historico(id: int):

    conta =  banco.buscar_conta(id)

    if not conta:
        return{"valor invalido"}
    
    historico = conta.listar_historico()
    return historico

@app.delete("/deletar_usuario")
def deletar(id: int):
    deletado = banco.deletar_usuario(id)

    if not deletado:
        return {"Usuario não deletado"}
    
    return{"Usuaurio deltado com sucesso"}