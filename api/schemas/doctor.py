from datetime import datetime
from pydantic import BaseModel


class CreateUpdate(BaseModel):
    doctor_code: str


class CreateUpdateSuccess(BaseModel):
    doctor_id: str
    doctor_code: str
    message: str

    class Config:
        orm_mode = True


class Doctor(BaseModel):
    doctor_id: str | None
    doctor_code: str | None
    user_id: str | None
    created_at: datetime | None
    updated_at: datetime | None

    class Config:
        orm_mode = True
