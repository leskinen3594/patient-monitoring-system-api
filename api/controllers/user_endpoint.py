from fastapi import APIRouter, HTTPException
from typing import List

from ..services.user import (
    create_user_service, get_all_user_service,get_one_user_service,
    update_user_service, delete_user_service, login_service
) 

from ..schemas.user import (
    CreateUpdate, CreateUpdateSuccess, DoctorLogin, LoginSuccess, PatientLogin, User, DeleteSuccess, Login
)

from ..handlers.errors import (
    DuplicateKeyException, NotFoundException, UnknowException
)


router = APIRouter()


@router.post("", response_model=CreateUpdateSuccess)
async def create(user: CreateUpdate):
    try:
        req_list = [t for t in user]
        user_id, response_msg = await create_user_service(user_request=req_list)
    except DuplicateKeyException as key_already_exist:
        raise HTTPException(status_code=400, detail=f"{key_already_exist}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")
    return CreateUpdateSuccess(user_id=user_id, message=response_msg)


@router.get("", response_model=List[User], response_model_exclude_none=True)
async def get_all():
    try:
        users = await get_all_user_service()
    except NotFoundException as error_not_found:
        raise HTTPException(status_code=204, detail=f"{error_not_found}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")
    return list(map(User.from_orm, users))


@router.get("/{user_id}", response_model=User, response_model_exclude_none=True)
async def get_by_id(user_id: str):
    try:
        user = await get_one_user_service(user_id)
    except NotFoundException as error_not_found:
        raise HTTPException(status_code=404, detail=f"{error_not_found}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")
    return user


@router.put("/{user_id}", response_model=CreateUpdateSuccess)
async def update(user_id: str, user: CreateUpdate):
    try:
        req_list = [t for t in user]
        response_msg = await update_user_service(user_id=user_id, user_request=req_list)
    except NotFoundException as error_not_found:
        raise HTTPException(status_code=404, detail=f"{error_not_found}")
    except UnknowException as error:
        raise HTTPException(status_code=400, detail=f"{error}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")
    return CreateUpdateSuccess(user_id=user_id, message=response_msg)


@router.delete("/{user_id}", response_model=DeleteSuccess)
async def delete(role_id: str):
    try:
        response_msg = await delete_user_service(role_id)
    except NotFoundException as error_not_found:
        raise HTTPException(status_code=404, detail=f"{error_not_found}")
    except UnknowException as error:
        raise HTTPException(status_code=400, detail=f"{error}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")
    return DeleteSuccess(message=response_msg)


# @router.post("/login", response_model=LoginSuccess | DoctorLogin | PatientLogin, response_model_exclude_none=True)
@router.post("/login")
async def login(login: Login):
    try:
        req_list = [t for t in login]
        user = await login_service(login_request=req_list)
    except NotFoundException as error_not_found:
        raise HTTPException(status_code=404, detail=f"{error_not_found}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")
    return user
    # if patient is None:
    #     return DoctorLogin(user_info=user, doctor_info=doctor)
