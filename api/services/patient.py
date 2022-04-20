from typing import List, Tuple

from ..handlers.utilities import datetime_set_timezone

from domain.usecase import (
    create_new_patient as __usecase_create,
    get_all_patient as __usecase_get_all,
    get_one_patient as __usecase_get_one,
    update_patient_info as __usecase_update
)


async def create_patient_service(patient_request: List[str]) -> Tuple[str]:
    return await __usecase_create(patient_request, datetime_set_timezone(7))


async def get_all_patient_service():
    return await __usecase_get_all()


async def get_one_patient_service(patient_id: str):
    return await __usecase_get_one(patient_id)


async def update_patient_service(patient_id: str, patient_request: List[str]) -> str:
    patient = await __usecase_get_one(patient_id)
    return await __usecase_update(patient, patient_request, datetime_set_timezone(7))