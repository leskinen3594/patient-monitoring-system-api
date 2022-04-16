import uuid
from typing import TYPE_CHECKING

from ..handlers.errors import (
    DuplicateKeyException, NotFoundException, UnknowException
)

from domain.port import RoleRepositoryAbstract
from ..models import all_tables as _models
from ..schemas.role import Role

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


class RoleRepository(RoleRepositoryAbstract):
    ''' Implement methods domain repository '''

    def __init__(self, database: "Session"):
        self.db = database


    async def generate_role_id(self) -> str:
        return str(uuid.uuid4())


    async def insert(self, role) -> str:
        try:
            self.role = _models.Role(**role)
            self.db.add(self.role)
            self.db.commit()
        except Exception as e:
            raise DuplicateKeyException(f"'role_nameth' or 'role_nameen' already exist. debug: {e}")
        return "role created"


    async def select_all(self) -> Role:
        try:
            self.roles = self.db.query(_models.Role).all()
        except Exception as e:
            raise NotFoundException(f"role empty. debug: {e}")
        return self.roles


    async def select_by_id(self, id: str) -> Role:
        try:
            self.role = self.db.query(_models.Role).filter(_models.Role.role_id == id).first()

            if self.role is None:
                raise
        except Exception as e:
            raise NotFoundException(f"role_id: '{id}' not found. debug: {e}")
        return self.role


    async def update(self, role: Role, role_update: Role) -> str:
        try:
            # print(f"\n [DEBUG 1] : {role_update} \n")
            role.role_nameth = role_update['role_nameth']
            role.role_nameen = role_update['role_nameen']
            role.updated_at = role_update['updated_at']

            self.db.commit()
        except Exception as e:
            raise UnknowException(f"cannot update role_id: '{role.role_id}'. debug: {e}")
        return "role updated"


    async def delete(self, role: Role):
        try:
            self.db.delete(role)
            self.db.commit()
        except Exception as e:
            raise UnknowException(f"cannot delete role_id: '{role.role_id}'. debug: {e}")
        return "role deleted"