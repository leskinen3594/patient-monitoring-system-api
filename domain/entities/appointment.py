from typing import Dict, List
from pydantic import BaseModel, Field
from datetime import datetime


class Appointment(BaseModel):
    apmt_id: str = Field(..., alias='apmt_id')
    pt_id: str = Field(..., alias='pt_id')
    doctor_id: str = Field(..., alias='doctor_id')
    apmt_datettime: datetime = Field(..., alias='apmt_datetime')
    created_at: datetime = Field(..., alias='created_at')
    updated_at: datetime = Field(..., alias='updated_at')

    def create_new_apmt_with_items(id: str, apmtList: List[str], createDate: datetime):
        apmt_dict: Dict[str, str | datetime] = {key: item for key, item in apmtList}
        id_dict = {'apmt_id': id}
        created_at_dict = {'created_at': createDate}
        apmt_dict.update(id_dict)
        apmt_dict.update(created_at_dict)

        return apmt_dict

    def update_apmt_with_id(apmtList: List[str], updateDate: datetime):
        apmt_dict: Dict[str, str | datetime] = {key: value for key, value in apmtList}
        updated_at_dict = {'updated_at': updateDate}
        apmt_dict.update(updated_at_dict)

        return apmt_dict