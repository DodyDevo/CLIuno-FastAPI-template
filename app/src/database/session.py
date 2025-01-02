from typing import AsyncGenerator

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.src.core.config import get_settings

settings = get_settings()

async_engine = create_async_engine(str(settings.async_postgres_url), echo=settings.DEBUG)

AsyncSessionLocal = async_sessionmaker(async_engine, expire_on_commit=False)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        try:
            yield session
        except HTTPException:
            await session.rollback()
            raise
        finally:
            await session.close()
