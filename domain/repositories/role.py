from abc import abstractmethod

from domain.base.repository import RepositoryAbstract
from domain.entities import Role


class RoleRepositoryAbstract(RepositoryAbstract[str, Role]):
    @abstractmethod
    async def generate_role_id(self):
        pass


    @abstractmethod
    async def select_all(self) -> Role:
        pass


    @abstractmethod
    async def select_by_id(self, id: str) -> Role:
        pass


    @abstractmethod
    async def insert(self, entity: Role):
        pass


    @abstractmethod
    async def update(self, entity: Role, updateInfo: Role):
        pass


    @abstractmethod
    async def delete(self, entity: Role):
        pass