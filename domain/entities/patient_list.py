from typing import Dict, List
from pydantic import BaseModel, Field


class PatientList(BaseModel):
    ptl_id: str = Field(..., alias='ptl_id')
    doctor_id: str = Field(..., alias='doctor_id')
    pt_id: str = Field(..., alias='pt_id')

    def create_new_ptl_with_items(id: str, ptlList: List[str]):
        ptl_dict: Dict[str, str] = {key: item for key, item in ptlList}
        id_dict = {'ptl_id': id}
        ptl_dict.update(id_dict)

        return ptl_dict

    def update_ptl_with_id(ptlList: List[str]):
        ptl_dict: Dict[str, str] = {key: value for key, value in ptlList}

        return ptl_dict
