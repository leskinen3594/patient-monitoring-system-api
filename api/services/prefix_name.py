from typing import List, Tuple

from ..handlers.utilities import datetime_set_timezone

from domain.usecase import (
    create_new_prefix as __usecase_create,
    get_all_prefix as __usecase_get_all,
    get_one_prefix as __usecase_get_one,
)


async def create_prefix_service(prefix_request: List[str]) -> Tuple[str]:
    return await __usecase_create(prefix_request, datetime_set_timezone(7))


async def get_all_prefix_service():
    return await __usecase_get_all()


async def get_one_prefix_service(prefix_id: str):
    return await __usecase_get_one(prefix_id)