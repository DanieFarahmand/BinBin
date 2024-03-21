import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.sqldb.base import SQLBase
from src.core.sqldb.mixins import TimestampMixin, IDMixin, UUIDMixin
from src.models.enums import UserRoleEnum


class User(SQLBase, IDMixin, UUIDMixin, TimestampMixin):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(
        sa.String(24),
        nullable=True
    )
    email: Mapped[str] = mapped_column(
        sa.String(28),
        nullable=False,
        unique=True,
    )
    password: Mapped[str] = mapped_column(
        sa.String,
        nullable=False
    )
    profile_image: Mapped[str] = mapped_column(
        sa.String,
        nullable=True
    )

    role: Mapped[UserRoleEnum] = mapped_column(
        sa.Enum(UserRoleEnum),
        default=UserRoleEnum.normal_user.value,
        nullable=False
    )
