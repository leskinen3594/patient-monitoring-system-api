from abc import abstractmethod

from domain.base.repository import RepositoryAbstract
from domain.entities import Doctor


class DoctorRepositoryAbstract(RepositoryAbstract[str, Doctor]):
    @abstractmethod
    async def generate_doctor_id(self):
        pass


    @abstractmethod
    async def select_all(self) -> Doctor:
        pass


    @abstractmethod
    async def select_by_id(self, id: str) -> Doctor:
        pass


    @abstractmethod
    async def insert(self, entity: Doctor):
        pass


    @abstractmethod
    async def update(self, entity: Doctor, updateInfo: Doctor):
        pass


    # @abstractmethod
    # async def delete(self, entity: Doctor):
    #     pass