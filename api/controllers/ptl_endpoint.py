from fastapi import APIRouter, HTTPException
from typing import List

from ..services.patient_list import (
    create_ptl_service, get_all_ptl_service, get_one_ptl_service,
    update_ptl_service, delete_ptl_service
) 

from ..schemas.patient_list import (
    CreateUpdate, CreateUpdateSuccess, DeleteSuccess, PatientList
)

from ..handlers.errors import (
    NotFoundException, UnknowException
)


router = APIRouter()


@router.post("", response_model=CreateUpdateSuccess)
async def create(ptl: CreateUpdate):
    try:
        req_list = [t for t in ptl]
        ptl_id, response_msg = await create_ptl_service(ptl_request=req_list)
    except UnknowException as error:
        raise HTTPException(status_code=400, detail=f"{error}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")
    return CreateUpdateSuccess(ptl_id=ptl_id, message=response_msg)


@router.get("", response_model=List[PatientList], response_model_exclude_none=True)
async def get_all():
    try:
        ptls = await get_all_ptl_service()
    except NotFoundException as error_not_found:
        raise HTTPException(status_code=204, detail=f"{error_not_found}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")
    return list(map(PatientList.from_orm, ptls))


@router.get("/{doctor_id}", response_model=PatientList, response_model_exclude_none=True)
async def get_by_id(doctor_id: str):
    try:
        ptl = await get_one_ptl_service(doctor_id)
    except NotFoundException as error_not_found:
        raise HTTPException(status_code=404, detail=f"{error_not_found}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")
    return ptl


@router.put("/{ptl_id}", response_model=CreateUpdateSuccess)
async def update(ptl_id: str, ptl: CreateUpdate):
    try:
        req_list = [t for t in ptl]
        response_msg = await update_ptl_service(ptl_id=ptl_id, ptl_request=req_list)
    except NotFoundException as error_not_found:
        raise HTTPException(status_code=404, detail=f"{error_not_found}")
    except UnknowException as error:
        raise HTTPException(status_code=400, detail=f"{error}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")
    return CreateUpdateSuccess(ptl_id=ptl_id, message=response_msg)


@router.delete("/{ptl_id}", response_model=DeleteSuccess)
async def delete(ptl_id: str):
    try:
        response_msg = await delete_ptl_service(ptl_id)
    except NotFoundException as error_not_found:
        raise HTTPException(status_code=404, detail=f"{error_not_found}")
    except UnknowException as error:
        raise HTTPException(status_code=400, detail=f"{error}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")
    return DeleteSuccess(message=response_msg)