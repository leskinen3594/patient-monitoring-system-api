import uuid
from typing import TYPE_CHECKING

from ..handlers.errors import (
    DuplicateKeyException, NotFoundException, UnknowException
)

from domain.port import UserRepositoryAbstract
from ..models import all_tables as _models
from ..schemas.user import (
    CreateUpdate, User
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
        except:
            raise DuplicateKeyException(f"this email already exist.")
        return "user created"


    async def select_all(self) -> User:
        try:
            self.users = self.db.query(_models.User).all()
        except:
            raise NotFoundException(f"user empty.")
        return self.users


    async def select_by_id(self, id: str) -> User:
        try:
            self.user = self.db.query(_models.User).filter(_models.User.user_id == id).first()

            if self.user is None:
                raise
        except:
            raise NotFoundException(f"user_id: '{id}' not found.")
        return self.user


    async def update(self, user: User, user_update: CreateUpdate) -> str:
        try:
            user.email = user_update['email']
            user.password = user_update['password']
            user.role_id = user_update['role_id']
            user.prefix_id = user_update['prefix_id']
            user.first_name = user_update['first_name']
            user.last_name = user_update['last_name']

            self.db.commit()
        except:
            raise DuplicateKeyException(f"this email already exist.")
        return "user updated"


    async def delete(self, user: User) -> str:
        try:
            self.db.delete(user)
            self.db.commit()
        except:
            raise UnknowException(f"cannot delete user_id: '{user.user_id}'.")
        return "user deleted"