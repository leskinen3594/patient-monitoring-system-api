from typing import Dict, List
from pydantic import BaseModel, Field
from datetime import datetime


class EstimateLog(BaseModel):
    log_id: str = Field(..., alias='log_id')
    doctor_id: str = Field(..., alias='doctor_id')
    pt_id: str = Field(..., alias='pt_id')
    log_level: int = Field(..., alias='log_level')
    log_desc: str = Field(..., alias='log_desc')
    created_at: datetime = Field(..., alias='created_at')
    updated_at: datetime = Field(..., alias='updated_at')

    def create_new_log_with_items(id: str, logList: List[str], createDate: datetime):
        log_dict: Dict[str, str | int | datetime] = {key: item for key, item in logList}
        id_dict = {'log_id': id}
        created_at_dict = {'created_at': createDate}
        log_dict.update(id_dict)
        log_dict.update(created_at_dict)

        return log_dict

    def update_log_with_id(logList: List[str], updateDate: datetime):
        log_dict: Dict[str, str | int | datetime] = {key: value for key, value in logList}
        updated_at_dict = {'updated_at': updateDate}
        log_dict.update(updated_at_dict)

        return log_dict
