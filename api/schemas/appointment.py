from datetime import datetime
from pydantic import BaseModel


class CreateUpdate(BaseModel):
    pt_id: str
    doctor_id: str
    apmt_datettime: datetime


class CreateUpdateSuccess(BaseModel):
    apmt_id: str
    message: str

    class Config:
        orm_mode = True


class Appointment(BaseModel):
    apmt_id: str | None
    pt_id: str | None
    doctor_id: str | None
    apmt_datettime: datetime | None
    created_at: datetime | None
    updated_at: datetime | None

    class Config:
        orm_mode = True


class DeleteSuccess(BaseModel):
    message: str

    class Config:
        orm_mode = True