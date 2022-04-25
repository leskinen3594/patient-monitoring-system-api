from fastapi import APIRouter, HTTPException
from typing import List

from ..services.appointment import (
    create_apmt_service, get_all_apmt_service, get_one_apmt_service,
    update_apmt_service, delete_apmt_service, get_one_apmt_by_id_service
) 

from ..schemas.appointment import (
    CreateUpdate, CreateUpdateSuccess, DeleteSuccess,
    Appointment
)

from ..handlers.errors import (
    NotFoundException, UnknowException
)


router = APIRouter()


@router.post("", response_model=CreateUpdateSuccess)
async def create(apmt: CreateUpdate):
    try:
        req_list = [t for t in apmt]
        apmt_id, response_msg = await create_apmt_service(apmt_request=req_list)
    except UnknowException as error:
        raise HTTPException(status_code=400, detail=f"{error}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")
    return CreateUpdateSuccess(apmt_id=apmt_id, message=response_msg)


@router.get("", response_model=List[Appointment], response_model_exclude_none=True)
async def get_all():
    try:
        all_apmt = await get_all_apmt_service()
    except NotFoundException as error_not_found:
        raise HTTPException(status_code=204, detail=f"{error_not_found}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")
    return list(map(Appointment.from_orm, all_apmt))


@router.get("/patients/{pt_id}", response_model=List[Appointment], response_model_exclude_none=True)
async def get_by_id(pt_id: str):
    try:
        apmts = await get_one_apmt_service(pt_id)
    except NotFoundException as error_not_found:
        raise HTTPException(status_code=404, detail=f"{error_not_found}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")
    return apmts


@router.get("/{apmt_id}", response_model=List[Appointment], response_model_exclude_none=True)
async def get_by_apmt_id(apmt_id: str):
    try:
        apmts = await get_one_apmt_by_id_service(apmt_id)
    except NotFoundException as error_not_found:
        raise HTTPException(status_code=404, detail=f"{error_not_found}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")
    return apmts


@router.put("/{apmt_id}", response_model=CreateUpdateSuccess)
async def update(apmt_id: str, apmt: CreateUpdate):
    try:
        req_list = [t for t in apmt]
        response_msg = await update_apmt_service(apmt_id=apmt_id, apmt_request=req_list)
    except NotFoundException as error_not_found:
        raise HTTPException(status_code=404, detail=f"{error_not_found}")
    except UnknowException as error:
        raise HTTPException(status_code=400, detail=f"{error}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")
    return CreateUpdateSuccess(apmt_id=apmt_id, message=response_msg)


@router.delete("/{apmt_id}", response_model=DeleteSuccess)
async def delete(apmt_id: str):
    try:
        response_msg = await delete_apmt_service(apmt_id)
    except NotFoundException as error_not_found:
        raise HTTPException(status_code=404, detail=f"{error_not_found}")
    except UnknowException as error:
        raise HTTPException(status_code=400, detail=f"{error}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")
    return DeleteSuccess(message=response_msg)