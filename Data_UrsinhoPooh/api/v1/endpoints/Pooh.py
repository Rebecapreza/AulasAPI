from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.personagens_model import PersonagensModel
from schemas.personagens_schema import PersonagensSchemas
from core.deps import get_session

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PersonagensSchemas)
async def post_personagem(personagens: PersonagensSchemas, db: AsyncSession = Depends(get_session)):
    novo_personagem = PersonagensModel(
        nome=personagens.nome,
        personalidade=personagens.personalidade,
        cor=personagens.cor
    )
    db.add(novo_personagem)
    await db.commit()          
    await db.refresh(novo_personagem)  
    return novo_personagem


@router.get("/", response_model=List[PersonagensSchemas])
async def get_personagem(db: AsyncSession = Depends(get_session)):
    query = select(PersonagensModel)
    result = await db.execute(query)
    pooh: List[PersonagensModel] = result.scalars().all()
    return pooh


@router.get("/{personagem_id}", response_model=PersonagensSchemas, status_code=status.HTTP_200_OK)
async def get_personagens(personagem_id: int, db: AsyncSession = Depends(get_session)):
    query = select(PersonagensModel).filter(PersonagensModel.id == personagem_id)
    result = await db.execute(query)
    pooh = result.scalar_one_or_none()
    if pooh:
        return pooh
    raise HTTPException(detail="Personagem não encontrado", status_code=status.HTTP_404_NOT_FOUND)


@router.put("/{personagem_id}", response_model=PersonagensSchemas, status_code=status.HTTP_202_ACCEPTED)
async def put_personagem(personagem_id: int, personagens: PersonagensSchemas, db: AsyncSession = Depends(get_session)):
    query = select(PersonagensModel).filter(PersonagensModel.id == personagem_id)
    result = await db.execute(query)
    pooh_up = result.scalar_one_or_none()
    if not pooh_up:
        raise HTTPException(detail="Personagem não encontrado", status_code=status.HTTP_404_NOT_FOUND)

    pooh_up.nome = personagens.nome
    pooh_up.personalidade = personagens.personalidade
    pooh_up.cor = personagens.cor

    await db.commit()
    await db.refresh(pooh_up)
    return pooh_up


@router.delete("/{personagem_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_personagem(personagem_id: int, db: AsyncSession = Depends(get_session)):
    query = select(PersonagensModel).filter(PersonagensModel.id == personagem_id)
    result = await db.execute(query)
    pooh_del = result.scalar_one_or_none()
    if not pooh_del:
        raise HTTPException(detail="Personagem não encontrado", status_code=status.HTTP_404_NOT_FOUND)

    await db.delete(pooh_del)
    await db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
