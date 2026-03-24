from fastapi import APIRouter
from app.modelos.cliente import Cliente

router = APIRouter(
    prefix='/clientes'
)

@router.get('/', response_model=list[Cliente])
async def listar_clientes():

    clientes_list = [Cliente(nome='Guilherme', email='ggserranodev@gmail.com', telefone='51993830517')]

    return clientes_list
