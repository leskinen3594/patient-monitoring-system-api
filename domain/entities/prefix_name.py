from typing import List, Dict
from pydantic import BaseModel, Field
from datetime import datetime


class PrefixName(BaseModel):
    prefix_id: str = Field(..., alias='prefix_id')
    prefix_nameth: str = Field(..., alias='prefix_nameth')
    prefix_nameen: str = Field(..., alias='prefix_nameen')
    prefix_ab_nameth: str = Field(..., alias='prefix_ab_nameth')
    prefix_ab_nameen: str = Field(..., alias='prefix_ab_nameen')
    created_at: datetime = Field(..., alias='created_at')
    updated_at: datetime = Field(..., alias='updated_at')

    def create_new_prefix_name_with_items(id: str, prefixList: List[str], createDate: datetime):
        prefix_dict: Dict[str, str | datetime] = {key: value for key, value in prefixList}
        id_dict = {'prefix_id': id}
        created_at_dict = {'created_at': createDate}
        prefix_dict.update(id_dict)
        prefix_dict.update(created_at_dict)

        return prefix_dict