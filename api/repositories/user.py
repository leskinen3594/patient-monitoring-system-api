import uuid
from typing import TYPE_CHECKING

from sqlalchemy import and_

from ..handlers.errors import (
    DuplicateKeyException, NotFoundException, UnknowException
)

from domain.port import UserRepositoryAbstract
from ..models import all_tables as _models
from ..schemas.user import (
    CreateUpdate, User, Login
)


if TYPE_CHECKING:
    from sqlalchemy.orm import Session


class UserRepository(UserRepositoryAbstract):
    ''' Implement methods domain repository '''

    def __init__(self, database: "Session"):
        self.db = database


    async def generate_user_id(self) -> str:
        return str(uuid.uuid4())


    async def insert(self, user: CreateUpdate) -> str:
        try:
            self.user = _models.User(**user)
            self.db.add(self.user)
            self.db.commit()
        except Exception as e:
            raise DuplicateKeyException(f"this email already exist. {e}")
        return "user created"


    async def select_all(self) -> User:
        try:
            self.users = self.db.query(_models.User).all()
        except Exception as e:
            raise NotFoundException(f"user empty. {e}")
        return self.users


    async def select_by_id(self, id: str) -> User:
        try:
            self.user = self.db.query(_models.User).filter(_models.User.user_id == id).first()

            if self.user is None:
                raise
        except Exception as e:
            raise NotFoundException(f"user_id: '{id}' not found. {e}")
        return self.user


    async def update(self, user: User, user_update: CreateUpdate) -> str:
        try:
            user.email = user_update['email']
            user.password = user_update['password']
            user.role_id = user_update['role_id']
            user.prefix_id = user_update['prefix_id']
            user.first_name = user_update['first_name']
            user.last_name = user_update['last_name']
            user.updated_at = user_update['updated_at']

            self.db.commit()
        except Exception as e:
            raise DuplicateKeyException(f"this email already exist. {e}")
        return "user updated"


    async def delete(self, user: User) -> str:
        try:
            self.db.delete(user)
            self.db.commit()
        except Exception as e:
            raise UnknowException(f"cannot delete user_id: '{user.user_id}'. {e}")
        return "user deleted"


    async def login(self, login: Login):
        try:
            self.user_info = self.db.query(_models.User.user_id,
                                           _models.User.email,
                                           _models.User.password,
                                           _models.User.role_id,
                                           _models.Role.role_nameen,
                                           _models.Role.role_nameth,
                                           _models.User.prefix_id,
                                           _models.PrefixName.prefix_nameen,
                                           _models.PrefixName.prefix_nameth,
                                           _models.PrefixName.prefix_ab_nameen,
                                           _models.PrefixName.prefix_ab_nameth,
                                           _models.User.first_name,
                                           _models.User.last_name,
                                           _models.User.created_at,
                                           _models.User.updated_at)\
                                    .join(_models.Role)\
                                    .join(_models.PrefixName)\
                                    .filter(
                                        and_(_models.User.email == login.email,
                                        _models.User.password == login.password))\
                                    .first()

            # self.user_info = self.db.query(_models.User,
            #                                _models.Role,
            #                                _models.PrefixName)\
            #                         .join(_models.Role)\
            #                         .join(_models.PrefixName)\
            #                         .filter(
            #                             and_(_models.User.email == login.email,
            #                             _models.User.password == login.password))\
            #                         .first()

            if self.user_info is None:
                raise
        except Exception as e:
            raise NotFoundException(f"email or password invalid. {e}")
        return self.user_info


    async def doctor_detail(self, userId: str):
        try:
            self.doctor_info = self.db.query(_models.Doctor)\
                                        .filter(_models.Doctor.user_id == userId)\
                                        .first()

            if self.doctor_info is None:
                raise
        except Exception as e:
            raise NotFoundException(f"doctor not found. {e}")
        return self.doctor_info


    async def patient_detail(self, userId: str):
        try:
            self.patient_info = self.db.query(_models.Patient)\
                                        .filter(_models.Patient.user_id == userId)\
                                        .first()
        except Exception as e:
            raise NotFoundException(f"patient not found. {e}")
        return self.patient_info