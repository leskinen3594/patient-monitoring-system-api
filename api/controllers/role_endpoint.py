from fastapi import APIRouter, HTTPException
from typing import List

from ..services.role import (
    create_role_service, get_all_role_service, get_one_role_service,
    update_role_service, delete_role_service
) 

from ..schemas.role import (
    CreateUpdateRole, CreateUpdateRoleSuccess, DeleteRoleSuccess,
    Role
)

from ..handlers.errors import (
    DuplicateKeyException, NotFoundException, UnknowException
)


router = APIRouter()


@router.post("", response_model=CreateUpdateRoleSuccess)
async def create(role: CreateUpdateRole):
    try:
        req_list = [t for t in role]
        role_id, response_msg = await create_role_service(role_request=req_list)
    except DuplicateKeyException as key_already_exist:
        raise HTTPException(status_code=400, detail=f"{key_already_exist}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")
    return CreateUpdateRoleSuccess(role_id=role_id, message=response_msg)


@router.get("", response_model=List[Role], response_model_exclude_none=True)
async def get_all():
    try:
        role = await get_all_role_service()
    except NotFoundException as error_not_found:
        raise HTTPException(status_code=404, detail=f"{error_not_found}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")
    return list(map(Role.from_orm, role))


@router.get("/{role_id}", response_model=Role, response_model_exclude_none=True)
async def get_by_id(role_id: str):
    try:
        role = await get_one_role_service(role_id)
    except NotFoundException as error_not_found:
        raise HTTPException(status_code=404, detail=f"{error_not_found}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")
    return role


@router.put("/{role_id}", response_model=CreateUpdateRoleSuccess)
async def update(role_id: str, role: CreateUpdateRole):
    try:
        req_list = [t for t in role]
        response_msg = await update_role_service(role_id=role_id, role_request=req_list)
    except NotFoundException as error_not_found:
        raise HTTPException(status_code=404, detail=f"{error_not_found}")
    except UnknowException as error:
        raise HTTPException(status_code=400, detail=f"{error}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")
    return CreateUpdateRoleSuccess(role_id=role_id, message=response_msg)


@router.delete("/{role_id}", response_model=DeleteRoleSuccess)
async def delete(role_id: str):
    try:
        response_msg = await delete_role_service(role_id)
    except NotFoundException as error_not_found:
        raise HTTPException(status_code=404, detail=f"{error_not_found}")
    except UnknowException as error:
        raise HTTPException(status_code=400, detail=f"{error}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")
    return DeleteRoleSuccess(message=response_msg)
