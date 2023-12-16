from typing import List

from .router import api_router
from app.api_models.response_models import ContaResponse
from app.api_models.request_models import AdicionarContaRequest

@api_router.get('/', response_model=List[ContaResponse])
async def listar_contas():
    conta_1 = ContaResponse(id=1, descricao="conta pagar 01", valor=20.0, tipo="PAGAR")
    conta_2 = ContaResponse(id=2, descricao="conta receber 02", valor=5.0, tipo="RECEBER")
    conta_3 = ContaResponse(id=3, descricao="conta pagar 03", valor=20.0, tipo="PAGAR")
    return [
        conta_1,
        conta_2,
        conta_3
    ]

@api_router.post("/add", response_model=ContaResponse)
async def adicionar_conta(conta: AdicionarContaRequest):
    add_conta_response = ContaResponse(
        descricao=conta.descricao,
        tipo=conta.tipo,
        valor=conta.valor,
        id=4
    )
    return add_conta_response



