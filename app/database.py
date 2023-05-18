from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from typing import TYPE_CHECKING

# from main import get_settings
from sqlalchemy import URL
from .config import Settings


if TYPE_CHECKING:
    from app.main import Application




class AsyncDatabaseSession:
    def __init__(self):
        self.session = None
        self._engine = None

    async def connect(self, app: "Application", settings: Settings):
        database_url = URL.create(
            drivername="postgresql+asyncpg",
            username=settings.database_user,
            password=settings.database_password,
            host=settings.database_host,
            port=settings.database_port,
            database=settings.database_name,
        )
        self._engine = create_async_engine(database_url, echo=True)
        self.session = sessionmaker(
            self._engine, class_=AsyncSession, expire_on_commit=False
        )

    async def disconnect(self):
        if self.session:
            await self.session().close()
        if self._engine:
            await self._engine.dispose()


db = AsyncDatabaseSession()
