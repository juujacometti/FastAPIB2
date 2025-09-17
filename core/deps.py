# Abre e fecha a conexão com o banco de dados 

from typing import Generator
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import Session

async def get_session() -> Generator:
    session: AsyncSession = Session()
    
    try: 
        yield session    # Mantém a sessão viva
    finally:
        await session.close    # Fecha a sessão