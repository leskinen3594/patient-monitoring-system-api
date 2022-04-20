from fastapi import APIRouter, HTTPException
from typing import List

from ..services.estimate_log import (
    create_log_service, get_all_log_service, get_one_log_service,
    update_log_service, delete_log_service
) 

from ..schemas.estimate_log import (
    CreateUpdate, CreateUpdateSuccess, DeleteSuccess, EstimateLog
)

from ..handlers.errors import (
    DuplicateKeyException, NotFoundException, UnknowException
)


router = APIRouter()


@router.post("", response_model=CreateUpdateSuccess)
async def create(log: CreateUpdate):
    try:
        req_list = [t for t in log]
        log_id, response_msg = await create_log_service(log_request=req_list)
    except UnknowException as insert_failed:
        raise HTTPException(status_code=400, detail=f"{insert_failed}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")
    return CreateUpdateSuccess(log_id=log_id, message=response_msg)


@router.get("", response_model=List[EstimateLog], response_model_exclude_none=True)
async def get_all():
    try:
        logs = await get_all_log_service()
    except NotFoundException as error_not_found:
        raise HTTPException(status_code=204, detail=f"{error_not_found}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")
    return list(map(EstimateLog.from_orm, logs))


@router.get("/{log_id}", response_model=EstimateLog, response_model_exclude_none=True)
async def get_by_id(log_id: str):
    try:
        estimate_log = await get_one_log_service(log_id)
    except NotFoundException as error_not_found:
        raise HTTPException(status_code=404, detail=f"{error_not_found}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")
    return estimate_log


@router.put("/{log_id}", response_model=CreateUpdateSuccess)
async def update(log_id: str, log: CreateUpdate):
    try:
        req_list = [t for t in log]
        response_msg = await update_log_service(log_id=log_id, log_request=req_list)
    except NotFoundException as error_not_found:
        raise HTTPException(status_code=404, detail=f"{error_not_found}")
    except UnknowException as error:
        raise HTTPException(status_code=400, detail=f"{error}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")
    return CreateUpdateSuccess(message=response_msg)


@router.delete("/{log_id}", response_model=DeleteSuccess)
async def delete(log_id: str):
    try:
        response_msg = await delete_log_service(log_id=log_id)
    except UnknowException as error:
        raise HTTPException(status_code=400, detail=f"{error}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")
    return DeleteSuccess(message=response_msg)