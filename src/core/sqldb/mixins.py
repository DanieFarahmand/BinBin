import uuid
import datetime

from sqlalchemy import BigInteger, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func


class TimestampMixin:
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime,
        default=func.now(),
        nullable=False
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        DateTime,
        default=func.now(),
        onupdate=func.now(),
        nullable=False
    )


class IDMixin:
    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        nullable=False,
        index=True,
        autoincrement=True
    )


class UUIDMixin:
    uuid: Mapped[str] = mapped_column(
        String,
        default=lambda: str(uuid.uuid4()),
        primary_key=True,
        nullable=False,
        index=True
    )
