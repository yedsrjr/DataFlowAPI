from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from tech_api.models import Animal, User
from tech_api.schemas import AnimalResponse, FilterPage
from tech_api.security import get_current_user, get_session

router = APIRouter(prefix="/animals", tags=["animals"])
DbSession = Annotated[AsyncSession, Depends(get_session)]
CurrentUser = Annotated[User, Depends(get_current_user)]


@router.get("/", status_code=HTTPStatus.OK, response_model=AnimalResponse)
async def read_animals(
    session: DbSession,
    filter_gado: Annotated[FilterPage, Query()],
    current_user: CurrentUser,
):
    if not current_user:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN, detail="Not enough permissions"
        )

    query = select(Animal)

    if filter_gado.status:
        status_normalizado = filter_gado.status.strip().lower()
        query = query.where(func.lower(func.trim(Animal.status)) == status_normalizado)

    if filter_gado.data_entrada_inicio and filter_gado.data_entrada_fim:
        query = query.where(
            Animal.data_entrada_fazenda.between(
                filter_gado.data_entrada_inicio, filter_gado.data_entrada_fim
            )
        )
    elif filter_gado.data_entrada_inicio:
        query = query.where(
            Animal.data_entrada_fazenda >= filter_gado.data_entrada_inicio
        )
    elif filter_gado.data_entrada_fim:
        query = query.where(Animal.data_entrada_fazenda <= filter_gado.data_entrada_fim)

    if filter_gado.data_saida_inicio and filter_gado.data_saida_fim:
        query = query.where(
            Animal.data_saida.between(
                filter_gado.data_saida_inicio, filter_gado.data_saida_fim
            )
        )
    elif filter_gado.data_saida_inicio:
        query = query.where(Animal.data_saida >= filter_gado.data_saida_inicio)
    elif filter_gado.data_saida_fim:
        query = query.where(Animal.data_saida <= filter_gado.data_saida_fim)

    query = query.offset(filter_gado.offset).limit(filter_gado.limit)

    result = await session.execute(query)
    animais = result.scalars().all()

    if not animais:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST, detail="Animals not found"
        )

    return {"animals": animais}
