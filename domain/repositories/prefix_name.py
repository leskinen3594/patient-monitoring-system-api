from abc import abstractmethod

from domain.base.repository import RepositoryAbstract
from domain.entities.prefix_name import PrefixName


class PrefixNameRepositoryAbstract(RepositoryAbstract[str, PrefixName]):
    @abstractmethod
    async def generate_prefix_id(self):
        pass


    @abstractmethod
    async def select_all(self) -> PrefixName:
        pass


    @abstractmethod
    async def select_by_id(self, id: str) -> PrefixName:
        pass


    @abstractmethod
    async def insert(self, entity: PrefixName):
        pass


    @abstractmethod
    async def update(self, entity: PrefixName, updateInfo: PrefixName):
        pass


    @abstractmethod
    async def delete(self, entity: PrefixName):
        pass