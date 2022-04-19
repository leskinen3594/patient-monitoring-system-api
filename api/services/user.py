from typing import List, Tuple

from api.schemas.user import DoctorBase, LoginSuccess, PatientBase, UserBase

from ..handlers.utilities import datetime_set_timezone

from domain.usecase import (
    create_new_user as __usecase_create,
    get_all_user as __usecase_get_all,
    get_one_user as __usecase_get_one,
    update_user_info as __usecase_update,
    delete_user as __usecase_delete,
    login_user as __usecase_login,
    login_doctor_detail as __usecase_doctor,
    login_patient_detail as __usecase_patient
)


async def create_user_service(user_request: List[str]) -> Tuple[str]:
    return await __usecase_create(user_request, datetime_set_timezone(7))


async def get_all_user_service():
    return await __usecase_get_all()


async def get_one_user_service(user_id: str):
    return await __usecase_get_one(user_id)


async def update_user_service(user_id: str, user_request: List[str]) -> str:
    user = await __usecase_get_one(user_id)
    return await __usecase_update(user, user_request, datetime_set_timezone(7))


async def delete_user_service(user_id: str):
    user = await __usecase_get_one(user_id)
    return await __usecase_delete(user)


async def login_service(login_request: List[str]):
    user_detail: UserBase = await __usecase_login(login_request)
    # print(f"\n [Debug 1] {user_detail[0]} \n")

    match user_detail.role_nameen:
        case "Doctor":
            doctor_detail: DoctorBase = await __usecase_doctor(user_detail.user_id)
            return [user_detail, doctor_detail]
        case "Patient":
            patient_detail: PatientBase = await __usecase_patient(user_detail.user_id)
            return [user_detail, patient_detail]
        case _:
            return [user_detail]