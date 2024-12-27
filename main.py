from fastapi import FastAPI
from typing import List, Dict


app = FastAPI()


dict_produtos: List[Dict[str, any]] = [
    {
        "id": 1,
        "nome": "Produto A",
        "preco": 19.99,
        "descricao": "Descrição do Produto A, com características e funcionalidades.",
        "categoria": "Categoria 1",
        "estoque": 100,
        "data_cadastro": "2024-12-27"
    },
    {
        "id": 2,
        "nome": "Produto B",
        "preco": 49.99,
        "descricao": "Descrição do Produto B, com características e funcionalidades.",
        "categoria": "Categoria 2",
        "estoque": 50,
        "data_cadastro": "2024-12-27"
    }
]



@app.get("/")
def home():
    return {"message":"Tudo certo"}


@app.get("/produtos")
def list_products():
    return dict_produtos

@app.get("/produtos/{id}")
def find_product(id:int):
    for produto in dict_produtos:
        if produto.get('id', None) == id:
            return produto
        
    return {"status":404, "message": "produto não encontrado"}