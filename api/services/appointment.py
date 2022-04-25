from typing import List, Tuple

from ..handlers.utilities import datetime_set_timezone

from domain.usecase import (
    create_new_apmt as __usecase_create,
    get_all_apmt as __usecase_get_all,
    get_one_apmt as __usecase_get_one,
    update_apmt_info as __usecase_update,
    delete_apmt as __usecase_delete,
    get_one_apmt_by_id as __usecase_get_one_id
)


async def create_apmt_service(apmt_request: List[str]) -> Tuple[str]:
    return await __usecase_create(apmt_request, datetime_set_timezone(7))


async def get_all_apmt_service():
    return await __usecase_get_all()


async def get_one_apmt_service(pt_id: str):
    return await __usecase_get_one(pt_id)


async def get_one_apmt_by_id_service(apmt_id: str):
    return await __usecase_get_one_id(apmt_id)


async def update_apmt_service(apmt_id: str, apmt_request: List[str]) -> str:
    apmt = await __usecase_get_one(apmt_id)
    return await __usecase_update(apmt, apmt_request, datetime_set_timezone(7))


async def delete_apmt_service(apmt_id: str):
    apmt = await __usecase_get_one(apmt_id)
    return await __usecase_delete(apmt)