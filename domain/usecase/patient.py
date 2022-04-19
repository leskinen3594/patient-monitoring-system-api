from datetime import datetime
from typing import List, Tuple

from domain.entities import Patient
from domain.registry import Registry


async def create_new_patient(partientReq: List[str], createdAt: datetime) -> Tuple[str]:
    repo = Registry().patient_repository
    patient_id: str = await repo.generate_patient_id()
    patient = Patient.create_new_patient_with_items(id=patient_id, patientList=partientReq, createDate=createdAt)
    patient_code, message = await repo.insert(patient)
    return (patient_id, patient_code, message)


async def get_all_patient() -> Patient:
    repo = Registry().patient_repository
    patients = await repo.select_all()
    return patients


async def get_one_patient(patientCode: str) -> Patient:
    repo = Registry().patient_repository
    patient = await repo.select_by_id(patientCode)
    return patient


async def update_patient_info(patient: Patient, patientReq: List[str], updatedAt: datetime) -> Tuple[str]:
    repo = Registry().patient_repository
    patient_update = Patient.update_patient_with_id(patientList=patientReq, updateDate=updatedAt)
    pt_id, message = await repo.update(patient, patient_update)
    return (pt_id, message)