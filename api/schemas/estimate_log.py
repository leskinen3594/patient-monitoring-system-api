from datetime import datetime
from pydantic import BaseModel


class CreateUpdate(BaseModel):
    doctor_id: str
    pt_id: str
    log_level: int
    log_desc: str | None


class CreateUpdateSuccess(BaseModel):
    message: str

    class Config:
        orm_mode = True


class EstimateLog(BaseModel):
    log_id: str | None
    doctor_id: str | None
    pt_id: str | None
    log_level: int | None
    log_desc: str | None
    created_at: datetime | None
    updated_at: datetime | None

    class Config:
        orm_mode = True


class DeleteSuccess(BaseModel):
    message: str

    class Config:
        orm_mode = True