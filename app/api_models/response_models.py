from decimal import Decimal
from pydantic import BaseModel

class ContaResponse(BaseModel):
    id: int
    descricao: str
    valor: Decimal
    tipo: str # PAGAR, RECEBER
