from datetime import datetime, date
from typing import Dict
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
    user_id: str | None
    email: str | None
    password: str | None
    role_id: str | None
    prefix_id: str | None
    first_name: str | None
    last_name: str | None
    created_at: datetime | None
    updated_at: datetime | None

    class Config:
        orm_mode = True


class DeleteSuccess(BaseModel):
    message: str

    class Config:
        orm_mode = True


class DoctorBase(BaseModel):
    doctor_id: str | None
    doctor_code: str | None
    user_id: str | None
    created_at: datetime | None
    updated_at: datetime | None

    class Config:
        orm_mode = True


class PatientBase(BaseModel):
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


class UserBase(BaseModel):
    user_id: str | None
    email: str | None
    password: str | None
    role_id: str | None
    role_nameth: str | None
    role_nameen: str | None
    prefix_id: str | None
    prefix_nameth: str | None
    prefix_nameen: str | None
    prefix_ab_nameth: str | None
    prefix_ab_nameen: str | None
    first_name: str | None
    last_name: str | None
    created_at: datetime | None
    updated_at: datetime | None

    class Config:
        orm_mode = True


class Login(BaseModel):
    email: str
    password: str


class LoginSuccess(BaseModel):
    user_info: UserBase | None

    class Config:
        orm_mode = True


class DoctorLogin(BaseModel):
    user_info: UserBase | None
    doctor_info: DoctorBase | None

    class Config:
        orm_mode = True


class PatientLogin(BaseModel):
    user_info: UserBase | None
    patient_info: PatientBase | None

    class Config:
        orm_mode = True