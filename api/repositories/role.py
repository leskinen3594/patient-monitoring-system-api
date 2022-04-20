import uuid
from typing import TYPE_CHECKING

from ..handlers.errors import (
    DuplicateKeyException, NotFoundException, UnknowException
)

from domain.port import RoleRepositoryAbstract
from ..models import all_tables as _models
from ..schemas.role import (
    CreateUpdateRole, Role
)


if TYPE_CHECKING:
    from sqlalchemy.orm import Session


class RoleRepository(RoleRepositoryAbstract):
    ''' Implement methods domain repository '''

    def __init__(self, database: "Session"):
        self.db = database


    async def generate_role_id(self) -> str:
        return str(uuid.uuid4())


    async def insert(self, role: CreateUpdateRole) -> str:
        try:
            self.role = _models.Role(**role)
            self.db.add(self.role)
            self.db.commit()
        except:
            raise DuplicateKeyException(f"'role_nameth' or 'role_nameen' already exist.")
        return "role created"


    async def select_all(self) -> Role:
        try:
            self.roles = self.db.query(_models.Role).all()
        except:
            raise NotFoundException(f"role empty.")
        return self.roles


    async def select_by_id(self, id: str) -> Role:
        try:
            self.role = self.db.query(_models.Role).filter(_models.Role.role_id == id).first()

            if self.role is None:
                raise
        except:
            raise NotFoundException(f"role_id: '{id}' not found.")
        return self.role


    async def update(self, role: Role, role_update: CreateUpdateRole) -> str:
        try:
            # print(f"\n [DEBUG 1] : {role_update} \n")
            role.role_nameth = role_update['role_nameth']
            role.role_nameen = role_update['role_nameen']
            role.updated_at = role_update['updated_at']

            self.db.commit()
        except:
            raise UnknowException(f"cannot update role_id: '{role.role_id}'.")
        return "role updated"


    async def delete(self, role: Role) -> str:
        try:
            self.db.delete(role)
            self.db.commit()
        except:
            raise UnknowException(f"cannot delete role_id: '{role.role_id}'.")
        return "role deleted"