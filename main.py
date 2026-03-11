from fastapi import FastAPI
from banco import Banco

app = FastAPI()

banco = Banco()

@app.post("/criarconta")
def criar_conta(nome: str, id: int):
    conta = banco.criar_conta(nome, id)
    return {"Mensagem": f"Conta criada para {conta.nome}"}


@app.post("/depositar")
def depositar(id: int, valor: float):
    conta = banco.buscar_conta(id)

    if conta is None:
        return {"erro": "Conta não encontrada"}

    saldo = conta.depositar(valor)
    return {"saldo": saldo}


@app.get("/buscarconta")
def buscar_conta(id: int):
    conta = banco.buscar_conta(id)

    if conta is None:
        return {"erro": "Conta não encontrada"}

    return {
        "nome": conta.nome,
        "saldo": conta.saldo
    }