from core.configs import settings
from core.database import engine 
from models import all_models

# Função para criar tabelas automaticamente 
async def create_tables() -> None:
    print("Criando tabelas no banco de dados")
    
    async with engine.begin() as conn:  
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)    # Deleta tudo
        
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)    # Cria tudo 
        
    print("Tabelas criadas com sucesso")
    
if __name__ == __main__:
    import asyncio
    
    asyncio.run(create_tables())