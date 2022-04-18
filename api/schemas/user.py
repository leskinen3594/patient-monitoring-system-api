from datetime import datetime
from pydantic import BaseModel


class CreateUpdate(BaseModel):
    email: str
    password: str
    role_id: str
    prefix_id: str
    first_name: str
    last_name: str


class CreateUpdateSuccess(BaseModel):
    user_id: str
    message: str

    class Config:
        orm_mode = True


class User(BaseModel):
    user_id: str
    email: str
    password: str
    role_id: str
    prefix_id: str
    first_name: str
    last_name: str
    created_at: datetime | None
    updated_at: datetime | None

    class Config:
        orm_mode = True


class DeleteSuccess(BaseModel):
    message: str

    class Config:
        orm_mode = True