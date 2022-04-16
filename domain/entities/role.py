from typing import Dict, List
from pydantic import BaseModel, Field
from datetime import datetime


class Role(BaseModel):
    role_id: str = Field(..., alias='role_id')
    role_nameth: str = Field(..., alias='role_nameth')
    role_nameen: str = Field(..., alias='role_nameen')
    created_at: datetime = Field(..., alias='created_at')
    updated_at: datetime = Field(..., alias='updated_at')
    # all_role: Dict[str, str | datetime]

    @classmethod
    def create_new_role_with_items(cls, *, id: str, roleList: List[str], createDate: datetime) -> 'Role':
        role_dict: Dict[str, str | datetime] = {key: item for key, item in roleList}
        id_dict = {'role_id': id}
        created_at_dict = {'created_at': createDate}
        role_dict.update(id_dict)
        role_dict.update(created_at_dict)
        # role = cls(all_role=role_dict)

        return role_dict

    def update_role_with_id(roleList: List[str], updateDate: datetime):
        role_dict: Dict[str, str | datetime] = {key: value for key, value in roleList}
        updated_at_dict = {'updated_at': updateDate}
        role_dict.update(updated_at_dict)

        return role_dict
