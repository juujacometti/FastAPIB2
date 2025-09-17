from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from core.configs import settings

engine: AsyncEngine = create_async_engine(settings.DB_URL)

Session: AsyncEngine = sessionmaker(
    autocommit = False,    # Evita commits automáticos dentro do banco de dados
    autoflush= False,
    expire_on_commit= False,     # Evita que a conexão seja encerrada ao acontecer um commit    
    class_= AsyncSession,
    bind= engine
)