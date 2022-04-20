from datetime import datetime
from pydantic import BaseModel


class CreateUpdate(BaseModel):
    prefix_nameth: str
    prefix_nameen: str | None
    prefix_ab_nameth: str
    prefix_ab_nameen: str | None


class CreateUpdateSuccess(BaseModel):
    prefix_id: str
    message: str

    class Config:
        orm_mode = True


class PrefixName(BaseModel):
    prefix_id: str
    prefix_nameth: str
    prefix_nameen: str | None
    prefix_ab_nameth: str
    prefix_ab_nameen: str | None
    created_at: datetime | None
    updated_at: datetime | None

    class Config:
        orm_mode = True