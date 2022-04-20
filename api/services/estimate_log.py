from typing import List, Tuple

from ..handlers.utilities import datetime_set_timezone

from domain.usecase import (
    create_new_log as __usecase_create,
    get_all_log as __usecase_get_all,
    get_one_log as __usecase_get_one,
    update_log_info as __usecase_update,
    delete_log as __usecase_delete,
)


async def create_log_service(log_request: List[str]) -> Tuple[str]:
    return await __usecase_create(log_request, datetime_set_timezone(7))


async def get_all_log_service():
    return await __usecase_get_all()


async def get_one_log_service(log_id: str):
    return await __usecase_get_one(log_id)


async def update_log_service(log_id: str, log_request: List[str]) -> str:
    estimate_log = await __usecase_get_one(log_id)
    return await __usecase_update(estimate_log, log_request, datetime_set_timezone(7))


async def delete_log_service(log_id: str):
    estimate_log = await __usecase_get_one(log_id)
    return await __usecase_delete(estimate_log)