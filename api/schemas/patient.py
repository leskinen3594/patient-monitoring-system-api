from datetime import datetime, date
from pydantic import BaseModel


class CreateUpdate(BaseModel):
    pt_code: str
    user_id: str
    identity_number: str
    pt_birth_date: date | None
    pt_religion: str | None
    pt_address: str | None
    pt_disease: str | None
    pt_weight: float | None
    pt_height: float | None
    pt_pressure: float | None
    pt_blood_type: str | None
    pt_remark: str | None

class CreateUpdateSuccess(BaseModel):
    pt_id: str
    pt_code: str
    message: str

    class Config:
        orm_mode = True


class Patient(BaseModel):
    pt_id: str | None
    pt_code: str | None
    user_id: str | None
    identity_number: str | None
    pt_birth_date: date | None
    pt_religion: str | None
    pt_address: str | None
    pt_disease: str | None
    pt_weight: float | None
    pt_height: float | None
    pt_pressure: float | None
    pt_blood_type: str | None
    pt_remark: str | None
    created_at: datetime | None
    updated_at: datetime | None

    class Config:
        orm_mode = True
