from datetime import datetime
from typing import List, Tuple

from domain.entities import Doctor
from domain.registry import Registry


async def create_new_doctor(doctorReq: List[str], createdAt: datetime) -> Tuple[str]:
    repo = Registry().doctor_repository
    doctor_id: str = await repo.generate_doctor_id()
    doctor = Doctor.create_new_doctor_with_items(id=doctor_id, doctorList=doctorReq, createDate=createdAt)
    doctor_code, message = await repo.insert(doctor)
    return (doctor_id, doctor_code, message)


async def get_all_doctor() -> Doctor:
    repo = Registry().doctor_repository
    doctors = await repo.select_all()
    return doctors


async def get_one_doctor(doctorId: str) -> Doctor:
    repo = Registry().doctor_repository
    doctor = await repo.select_by_id(doctorId)
    return doctor


async def update_doctor_info(doctor: Doctor, doctorReq: List[str], updatedAt: datetime) -> Tuple[str]:
    repo = Registry().doctor_repository
    doctor_update = Doctor.update_doctor_with_id(doctorList=doctorReq, updateDate=updatedAt)
    doctor_id, message = await repo.update(doctor, doctor_update)
    return (doctor_id, message)
