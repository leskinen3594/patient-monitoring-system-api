from datetime import datetime
from typing import List, Tuple

from domain.entities.role import Role
from domain.registry import Registry


async def create_new_role(roleReq: List[str], createdAt: datetime) -> Tuple[str]:
    repo = Registry().role_repository
    role_id: str = await repo.generate_role_id()
    role = Role.create_new_role_with_items(id=role_id, roleList=roleReq, createDate=createdAt)
    message = await repo.insert(role)
    return (role_id, message)


async def get_all_role() -> Role:
    repo = Registry().role_repository
    roles = await repo.select_all()
    return roles


async def get_one_role(roleId: str) -> Role:
    repo = Registry().role_repository
    role = await repo.select_by_id(roleId)
    return role


async def update_role_info(role: Role, roleReq: List[str], updatedAt: datetime) -> str:
    repo = Registry().role_repository
    role_update = Role.update_role_with_id(roleList=roleReq, updateDate=updatedAt)
    message = await repo.update(role, role_update)
    return message


async def delete_role(role: Role):
    repo = Registry().role_repository
    message = await repo.delete(role)
    return message