from datetime import datetime
from typing import List, Tuple

from domain.entities import PrefixName
from domain.registry import Registry


async def create_new_prefix(prefixReq: List[str], createdAt: datetime) -> Tuple[str]:
    repo = Registry().prefix_name_repository
    prefix_id: str = await repo.generate_prefix_id()
    prefix_name = PrefixName.create_new_prefix_name_with_items(id=prefix_id, prefixList=prefixReq, createDate=createdAt)
    message = await repo.insert(prefix_name)
    return (prefix_id, message)


async def get_all_prefix() -> PrefixName:
    repo = Registry().prefix_name_repository
    all_prefix_name = await repo.select_all()
    return all_prefix_name


async def get_one_prefix(prefixId: str) -> PrefixName:
    repo = Registry().prefix_name_repository
    prefix_name = await repo.select_by_id(prefixId)
    return prefix_name


async def update_prefix_info(prefix: PrefixName, prefixReq: List[str], updatedAt: datetime) -> str:
    pass


async def delete_prefix(prefix: PrefixName):
    pass