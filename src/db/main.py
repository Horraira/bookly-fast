from sqlmodel import SQLModel, create_engine, text
from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import Config

engine = AsyncEngine(
    create_engine(
        url=Config.DATABASE_URL,
        echo=True,
    )
)


async def init_db() -> None:
    async with engine.begin() as conn:
        # Here you can create your database tables
        statement = text("SELECT 'hello';")
        result = await conn.execute(statement)
        print(result.all())

        # await conn.run_sync(SQLModel.metadata.create_all)
