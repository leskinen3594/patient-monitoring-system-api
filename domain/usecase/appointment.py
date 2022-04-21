from datetime import datetime
from typing import List, Tuple

from domain.entities import Appointment
from domain.registry import Registry


async def create_new_apmt(apmtReq: List[str], createdAt: datetime) -> Tuple[str]:
    repo = Registry().apmt_repository
    apmt_id: str = await repo.generate_apmt_id()
    apmt = Appointment.create_new_apmt_with_items(id=apmt_id, apmtList=apmtReq, createDate=createdAt)
    message = await repo.insert(apmt)
    return (apmt_id, message)


async def get_all_apmt() -> Appointment:
    repo = Registry().apmt_repository
    all_apmt = await repo.select_all()
    return all_apmt


async def get_one_apmt(apmtId: str) -> Appointment:
    repo = Registry().apmt_repository
    apmt = await repo.select_by_id(apmtId)
    return apmt


async def update_apmt_info(apmt: Appointment, apmtReq: List[str], updatedAt: datetime) -> str:
    repo = Registry().apmt_repository
    apmt_update = Appointment.update_apmt_with_id(apmtList=apmtReq, updateDate=updatedAt)
    message = await repo.update(apmt, apmt_update)
    return message


async def delete_apmt(apmt: Appointment):
    repo = Registry().apmt_repository
    message = await repo.delete(apmt)
    return message