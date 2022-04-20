from fastapi import APIRouter, HTTPException
from typing import List

from ..services.doctor import (
    create_doctor_service, get_all_doctor_service, get_one_doctor_service,
    update_doctor_service
) 

from ..schemas.doctor import (
    CreateUpdate, CreateUpdateSuccess, Doctor
)

from ..handlers.errors import (
    DuplicateKeyException, NotFoundException, UnknowException
)


router = APIRouter()


@router.post("", response_model=CreateUpdateSuccess)
async def create(doctor: CreateUpdate):
    try:
        req_list = [t for t in doctor]
        doctor_id, doctor_code, response_msg = await create_doctor_service(doctor_request=req_list)
    except DuplicateKeyException as key_already_exist:
        raise HTTPException(status_code=400, detail=f"{key_already_exist}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")
    return CreateUpdateSuccess(doctor_id=doctor_id, doctor_code=doctor_code, message=response_msg)


@router.get("", response_model=List[Doctor], response_model_exclude_none=True)
async def get_all():
    try:
        doctors = await get_all_doctor_service()
    except NotFoundException as error_not_found:
        raise HTTPException(status_code=204, detail=f"{error_not_found}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")
    return list(map(Doctor.from_orm, doctors))


@router.get("/{doctor_code}", response_model=Doctor, response_model_exclude_none=True)
async def get_by_code(doctor_code: str):
    try:
        doctor = await get_one_doctor_service(doctor_code)
    except NotFoundException as error_not_found:
        raise HTTPException(status_code=404, detail=f"{error_not_found}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")
    return doctor


@router.put("/{doctor_code}", response_model=CreateUpdateSuccess)
async def update(doctor_code: str, doctor: CreateUpdate):
    try:
        req_list = [t for t in doctor]
        doctor_id, response_msg = await update_doctor_service(doctor_code=doctor_code, doctor_request=req_list)
    except NotFoundException as error_not_found:
        raise HTTPException(status_code=404, detail=f"{error_not_found}")
    except UnknowException as error:
        raise HTTPException(status_code=400, detail=f"{error}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")
    return CreateUpdateSuccess(doctor_id=doctor_id, doctor_code=doctor.doctor_code, message=response_msg)