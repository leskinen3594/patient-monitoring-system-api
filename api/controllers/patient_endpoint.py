from fastapi import APIRouter, HTTPException
from typing import List

from ..services.patient import (
    create_patient_service, get_all_patient_service, get_one_patient_service,
    update_patient_service
) 

from ..schemas.patient import (
    CreateUpdate, CreateUpdateSuccess, Patient
)

from ..handlers.errors import (
    DuplicateKeyException, NotFoundException, RequireKeyException
)


router = APIRouter()


@router.post("", response_model=CreateUpdateSuccess)
async def create(patient: CreateUpdate):
    try:
        req_list = [t for t in patient]
        patient_id, patient_code, response_msg = await create_patient_service(patient_request=req_list)
    except DuplicateKeyException as key_already_exist:
        raise HTTPException(status_code=400, detail=f"{key_already_exist}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")
    return CreateUpdateSuccess(pt_id=patient_id, pt_code=patient_code, message=response_msg)


@router.get("", response_model=List[Patient], response_model_exclude_none=True)
async def get_all():
    try:
        patients = await get_all_patient_service()
    except NotFoundException as error_not_found:
        raise HTTPException(status_code=204, detail=f"{error_not_found}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")
    return list(map(Patient.from_orm, patients))


@router.get("/{patient_code}", response_model=Patient, response_model_exclude_none=True)
async def get_by_code(patient_code: str):
    try:
        patient = await get_one_patient_service(patient_code)
    except NotFoundException as error_not_found:
        raise HTTPException(status_code=404, detail=f"{error_not_found}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")
    return patient


@router.put("/{patient_code}", response_model=CreateUpdateSuccess)
async def update(patient_code: str, patient: CreateUpdate):
    try:
        req_list = [t for t in patient]
        patient_id, response_msg = await update_patient_service(patient_code=patient_code, patient_request=req_list)
    except NotFoundException as error_not_found:
        raise HTTPException(status_code=404, detail=f"{error_not_found}")
    except RequireKeyException as error_require_key:
        raise HTTPException(status_code=400, detail=f"{error_require_key}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")
    return CreateUpdateSuccess(pt_id=patient_id, pt_code=patient.pt_code, message=response_msg)