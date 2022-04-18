from datetime import datetime
from typing import List, Tuple

from domain.entities import User
from domain.registry import Registry


async def create_new_user(userReq: List[str], createdAt: datetime) -> Tuple[str]:
    repo = Registry().user_repository
    user_id: str = await repo.generate_user_id()
    user = User.create_new_user_with_items(id=user_id, userList=userReq, createDate=createdAt)
    message = await repo.insert(user)
    return (user_id, message)


async def get_all_user() -> User:
    repo = Registry().user_repository
    users = await repo.select_all()
    return users


async def get_one_user(userId: str) -> User:
    repo = Registry().user_repository
    user = await repo.select_by_id(userId)
    return user


async def update_user_info(user: User, userReq: List[str], updatedAt: datetime) -> str:
    repo = Registry().user_repository
    user_update = User.update_user_with_id(userList=userReq, updateDate=updatedAt)
    message = await repo.update(user, user_update)
    return message


async def delete_user(user: User):
    repo = Registry().user_repository
    message = await repo.delete(user)
    return message