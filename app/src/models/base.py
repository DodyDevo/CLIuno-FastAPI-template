import uuid as uuid_pkg
from datetime import datetime
from typing import Optional

from sqlalchemy import text
from sqlmodel import DateTime, Field, SQLModel


class BaseModel(SQLModel):
    id: Optional[uuid_pkg.UUID] = Field(
        default_factory=uuid_pkg.uuid4,
        index=True,
        nullable=False,
        sa_column_kwargs={"server_default": text("gen_random_uuid()"), "unique": True},
        primary_key=True,
    )
    created_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(),
        sa_type=DateTime(timezone=True),
        sa_column_kwargs={"server_default": text("timezone('utc', now())")},
        nullable=False,
    )
    updated_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(),
        sa_type=DateTime(timezone=True),
        sa_column_kwargs={"onupdate": datetime.now()},
        nullable=False,
    )

    __mapper_args__ = {"polymorphic_on": "type", "polymorphic_identity": "base"}
