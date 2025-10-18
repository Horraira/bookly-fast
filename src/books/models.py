from sqlmodel import SQLModel, Field, Column
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime
from uuid import UUID, uuid4


class Book(SQLModel, table=True):
    __tablename__ = "books"
    uid: UUID = Field(
        sa_column=Column(
            pg.UUID(as_uuid=True),
            primary_key=True,
            nullable=False,
            default=uuid4,
        )
    )
    title: str | None = None
    author: str | None = None
    publisher: str | None = None
    publication_year: int | None = None
    pages: int | None = None
    language: str | None = None
    created_at: datetime = Field(Column(pg.TIMESTAMP, default=datetime.now))
    updated_at: datetime = Field(
        Column(pg.TIMESTAMP, default=datetime.now, onupdate=datetime.now)
    )

    def __repr__(self) -> str:
        return f"<Book(title={self.title}, author={self.author})>"
