from fastapi import APIRouter, HTTPException
from typing import List

from ..services.prefix_name import (
    create_prefix_service, get_all_prefix_service,
    get_one_prefix_service
) 

from ..schemas.prefix_name import (
    CreateUpdate, CreateUpdateSuccess, PrefixName
)

from ..handlers.errors import (
    NotFoundException, RequireKeyException
)


router = APIRouter()


@router.post("", response_model=CreateUpdateSuccess)
async def create(prefix_name: CreateUpdate):
    try:
        req_list = [t for t in prefix_name]
        prefix_id, response_msg = await create_prefix_service(prefix_request=req_list)
    except RequireKeyException as require_error:
        raise HTTPException(status_code=400, detail=f"{require_error}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")
    return CreateUpdateSuccess(prefix_id=prefix_id, message=response_msg)


@router.get("", response_model=List[PrefixName], response_model_exclude_none=True)
async def get_all():
    try:
        all_prefix_name = await get_all_prefix_service()
    except NotFoundException as error_not_found:
        raise HTTPException(status_code=204, detail=f"{error_not_found}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")
    return list(map(PrefixName.from_orm, all_prefix_name))


@router.get("/{prefix_id}", response_model=PrefixName, response_model_exclude_none=True)
async def get_by_id(prefix_id: str):
    try:
        prefix_name = await get_one_prefix_service(prefix_id)
    except NotFoundException as error_not_found:
        raise HTTPException(status_code=404, detail=f"{error_not_found}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")
    return prefix_name