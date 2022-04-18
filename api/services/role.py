from typing import List, Tuple

from ..handlers.utilities import datetime_set_timezone

from domain.usecase import (
    create_new_role as __usecase_create,
    get_all_role as __usecase_get_all,
    get_one_role as __usecase_get_one,
    update_role_info as __usecase_update,
    delete_role as __usecase_delete,
)


async def create_role_service(role_request: List[str]) -> Tuple[str]:
    return await __usecase_create(role_request, datetime_set_timezone(7))


async def get_all_role_service():
    return await __usecase_get_all()


async def get_one_role_service(role_id: str):
    return await __usecase_get_one(role_id)


async def update_role_service(role_id: str, role_request: List[str]) -> str:
    role = await __usecase_get_one(role_id)
    return await __usecase_update(role, role_request, datetime_set_timezone(7))


async def delete_role_service(role_id: str):
    role = await __usecase_get_one(role_id)
    return await __usecase_delete(role)