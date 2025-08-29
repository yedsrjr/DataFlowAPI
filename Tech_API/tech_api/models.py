from datetime import date, datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, registry

table_registry = registry()


@table_registry.mapped_as_dataclass
class Animal:
    __tablename__ = "animais"

    docentry: Mapped[int] = mapped_column(primary_key=True)
    baia: Mapped[str]
    lote: Mapped[str]
    idade_mes: Mapped[int]
    chip_bosch: Mapped[str] = mapped_column(nullable=True)
    num_sisbov: Mapped[str] = mapped_column(nullable=True)
    sexo: Mapped[str]
    raca: Mapped[str]
    status: Mapped[str]
    data_entrada_fazenda: Mapped[date] = mapped_column(nullable=True)
    peso_balancinha: Mapped[float] = mapped_column(nullable=True)
    data_processamento: Mapped[date] = mapped_column(nullable=True)
    data_saida: Mapped[date] = mapped_column(nullable=True)
    peso_saida: Mapped[float] = mapped_column(nullable=True)
    proprietario: Mapped[str]


@table_registry.mapped_as_dataclass
class User:
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    created_at: Mapped[datetime] = mapped_column(init=False, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now(), onupdate=func.now()
    )
