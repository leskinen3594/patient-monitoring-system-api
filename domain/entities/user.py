from typing import Dict, List
from pydantic import BaseModel, Field
from datetime import datetime


class User(BaseModel):
    user_id: str = Field(..., alias='user_id')
    email: str = Field(..., alias='email')
    password: str = Field(..., alias='password')
    role_id: str = Field(..., alias='role_id')
    prefix_id: str = Field(..., alias='prefix_id')
    first_name: str = Field(..., alias='first_name')
    last_name: str = Field(..., alias='last_name')
    created_at: datetime = Field(..., alias='created_at')
    updated_at: datetime = Field(..., alias='updated_at')


    def create_new_user_with_items(id: str, userList: List[str], createDate: datetime):
        user_dict: Dict[str, str | datetime] = {key: value for key, value in userList}
        id_dict = {'user_id': id}
        created_at_dict = {'created_at': createDate}
        user_dict.update(id_dict)
        user_dict.update(created_at_dict)

        return user_dict


    def update_user_with_id(userList: List[str], updateDate: datetime):
        user_dict: Dict[str, str | datetime] = {key: value for key, value in userList}
        updated_at_dict = {'updated_at': updateDate}
        user_dict.update(updated_at_dict)

        return user_dict
