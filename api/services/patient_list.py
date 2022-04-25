from typing import List, Tuple

from domain.usecase import (
    create_new_ptl as __usecase_create,
    get_all_ptl as __usecase_get_all,
    get_one_ptl as __usecase_get_one,
    update_ptl_info as __usecase_update,
    delete_ptl as __usecase_delete,
)


async def create_ptl_service(ptl_request: List[str]) -> Tuple[str]:
    return await __usecase_create(ptl_request)


async def get_all_ptl_service():
    return await __usecase_get_all()


async def get_one_ptl_service(doctor_id: str):
    return await __usecase_get_one(doctor_id)


async def update_ptl_service(ptl_id: str, ptl_request: List[str]) -> str:
    ptl = await __usecase_get_one(ptl_id)
    return await __usecase_update(ptl, ptl_request)


async def delete_ptl_service(ptl_id: str):
    ptl = await __usecase_get_one(ptl_id)
    return await __usecase_delete(ptl)