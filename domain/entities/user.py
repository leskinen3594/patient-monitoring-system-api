from typing import Dict, List
from pydantic import BaseModel, Field
from datetime import datetime, date


class User(BaseModel):
    user_id: str = Field(..., alias='user_id')
    email: str = Field(..., alias='email')
    password: str = Field(..., alias='password')
    role_id: str = Field(..., alias='role_id')
    prefix_id: str = Field(..., alias='prefix_id')
    first_name: str = Field(..., alias='first_name')
    last_name: str = Field(..., alias='last_name')
    created_at: datetime = Field(..., alias='created_at')
    updated_at: datetime = Field(..., alias='updated_at')


    def create_new_user_with_items(id: str, userList: List[str], createDate: datetime):
        user_dict: Dict[str, str | datetime] = {key: value for key, value in userList}
        id_dict = {'user_id': id}
        created_at_dict = {'created_at': createDate}
        user_dict.update(id_dict)
        user_dict.update(created_at_dict)

        return user_dict


    def update_user_with_id(userList: List[str], updateDate: datetime):
        user_dict: Dict[str, str | datetime] = {key: value for key, value in userList}
        updated_at_dict = {'updated_at': updateDate}
        user_dict.update(updated_at_dict)

        return user_dict


class Login(BaseModel):
    email: str = Field(..., alias='email')
    password: str = Field(..., alias='password')


    @classmethod
    def login_with_email(cls, *, loginList: List[str]):
        login_dict: Dict[str, str] = {key: value for key, value in loginList}
        login = cls(email=login_dict['email'], password=login_dict['password'])

        return login


class Doctor(BaseModel):
    doctor_id: str = Field(..., alias='doctor_id')
    doctor_code: str = Field(..., alias='doctor_code')
    user_id: str = Field(..., alias='user_id')
    created_at: datetime = Field(..., alias='created_at')
    updated_at: datetime = Field(..., alias='updated_at')


    def create_new_doctor_with_items(id: str, doctorList: List[str], createDate: datetime):
        doctor_dict: Dict[str, str | datetime] = {key: value for key, value in doctorList}
        id_dict = {'doctor_id': id}
        created_at_dict = {'created_at': createDate}
        doctor_dict.update(id_dict)
        doctor_dict.update(created_at_dict)

        return doctor_dict


    def update_doctor_with_id(doctorList: List[str], updateDate: datetime):
        doctor_dict: Dict[str, str | datetime] = {key: value for key, value in doctorList}
        updated_at_dict = {'updated_at': updateDate}
        doctor_dict.update(updated_at_dict)

        return doctor_dict


class Patient(BaseModel):
    pt_id: str = Field(..., alias='pt_id')
    pt_code: str = Field(..., alias='pt_code')
    user_id: str = Field(..., alias='user_id')
    identity_number: str = Field(..., alias='identity_number')
    pt_birth_date: date = Field(..., alias='pt_birth_date')
    pt_religion: str = Field(..., alias='pt_religion')
    pt_address: str = Field(..., alias='pt_address')
    pt_disease: str = Field(..., alias='pt_disease')
    pt_weight: float = Field(..., alias='pt_weight')
    pt_height: float = Field(..., alias='pt_height')
    pt_pressure: float = Field(..., alias='pt_pressure')
    pt_blood_type: str = Field(..., alias='pt_blood_type')
    pt_remark: str = Field(..., alias='pt_remark')
    created_at: datetime = Field(..., alias='created_at')
    updated_at: datetime = Field(..., alias='updated_at')

    def create_new_patient_with_items(id: str, patientList: List[str], createDate: datetime):
        patient_dict: Dict[str, str | float | date | datetime] = {key: value for key, value in patientList}
        id_dict = {'pt_id': id}
        created_at_dict = {'created_at': createDate}
        patient_dict.update(id_dict)
        patient_dict.update(created_at_dict)

        return patient_dict


    def update_patient_with_id(patientList: List[str], updateDate: datetime):
        patient_dict: Dict[str, str | float | date | datetime] = {key: value for key, value in patientList}
        updated_at_dict = {'updated_at': updateDate}
        patient_dict.update(updated_at_dict)

        return patient_dict