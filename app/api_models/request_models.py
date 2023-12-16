from decimal import Decimal
from pydantic import BaseModel

class AdicionarContaRequest(BaseModel):
    descricao: str
    valor: Decimal
    tipo: str