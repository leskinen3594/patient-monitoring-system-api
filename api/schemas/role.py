from datetime import datetime
from pydantic import BaseModel


class CreateUpdateRole(BaseModel):
    role_nameth: str
    role_nameen: str


class CreateUpdateRoleSuccess(BaseModel):
    role_id: str
    message: str

    class Config:
        orm_mode = True


class Role(BaseModel):
    role_id: str
    role_nameth: str | None
    role_nameen: str
    created_at: datetime | None
    updated_at: datetime | None

    class Config:
        orm_mode = True


class DeleteRoleSuccess(BaseModel):
    message: str

    class Config:
        orm_mode = True