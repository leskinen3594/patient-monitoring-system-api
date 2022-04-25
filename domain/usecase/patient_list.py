from typing import List, Tuple

from domain.entities import PatientList
from domain.registry import Registry


async def create_new_ptl(ptlReq: List[str]) -> Tuple[str]:
    repo = Registry().ptl_repository
    ptl_id: str = await repo.generate_ptl_id()
    patient_list = PatientList.create_new_ptl_with_items(id=ptl_id, ptlList=ptlReq)
    message = await repo.insert(patient_list)
    return (ptl_id, message)


async def get_all_ptl() -> PatientList:
    repo = Registry().ptl_repository
    all_ptl = await repo.select_all()
    return all_ptl


async def get_one_ptl(doctorId: str) -> PatientList:
    repo = Registry().ptl_repository
    patient_list = await repo.select_by_id(doctorId)
    return patient_list


async def update_ptl_info(ptl: PatientList, ptlReq: List[str]) -> str:
    repo = Registry().ptl_repository
    ptl_update = PatientList.update_ptl_with_id(ptlList=ptlReq)
    message = await repo.update(ptl, ptl_update)
    return message


async def delete_ptl(ptl: PatientList):
    repo = Registry().ptl_repository
    message = await repo.delete(ptl)
    return message