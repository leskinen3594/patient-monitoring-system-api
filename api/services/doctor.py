from typing import List, Tuple

from ..handlers.utilities import datetime_set_timezone

from domain.usecase import (
    create_new_doctor as __usecase_create,
    get_all_doctor as __usecase_get_all,
    get_one_doctor as __usecase_get_one,
    update_doctor_info as __usecase_update
)


async def create_doctor_service(doctor_request: List[str]) -> Tuple[str]:
    return await __usecase_create(doctor_request, datetime_set_timezone(7))


async def get_all_doctor_service():
    return await __usecase_get_all()


async def get_one_doctor_service(doctor_id: str):
    return await __usecase_get_one(doctor_id)


async def update_doctor_service(doctor_id: str, doctor_request: List[str]) -> str:
    doctor = await __usecase_get_one(doctor_id)
    return await __usecase_update(doctor, doctor_request, datetime_set_timezone(7))