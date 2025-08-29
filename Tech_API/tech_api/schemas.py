from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    id: int
    username: str
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)


class AnimalOut(BaseModel):
    docentry: int
    baia: str
    lote: str
    idade_mes: int
    chip_bosch: Optional[str] = None
    num_sisbov: str
    sexo: str
    raca: str
    status: str
    data_entrada_fazenda: date
    peso_balancinha: float
    data_processamento: date
    data_saida: Optional[date] = None
    peso_saida: Optional[float] = None
    proprietario: str
    model_config = ConfigDict(from_attributes=True)


class UserList(BaseModel):
    users: list[UserPublic]


class AnimalResponse(BaseModel):
    animals: list[AnimalOut]


class Token(BaseModel):
    access_token: str
    token_type: str


class FilterPage(BaseModel):
    offset: int = 0
    limit: int = 20
    status: Optional[str] = None
    data_entrada_inicio: date = Field(default=None, alias="data_entrada_inicio")
    data_entrada_fim: date = Field(default=None, alias="data_entrada_fim")
    data_saida_inicio: date = Field(default=None, alias="data_saida_inicio")
    data_saida_fim: date = Field(default=None, alias="data_saida_fim")
