from typing import List
from . import router

@router.get('/')
def listar_contas() -> List:
    return []

@router.post('add/')
def adicionar_conta(conta: object) -> object:
    return []

@router.put('edit/')
def editar_conta(conta: object) -> object:
    return []

@router.delete('delete/')
def deletar_conta(conta: object) -> object:
    return []



