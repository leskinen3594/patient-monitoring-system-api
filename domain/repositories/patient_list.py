from abc import abstractmethod

from domain.base.repository import RepositoryAbstract
from domain.entities import PatientList


class PatientListRepositoryAbstract(RepositoryAbstract[str, PatientList]):
    @abstractmethod
    async def generate_ptl_id(self):
        pass


    @abstractmethod
    async def select_all(self) -> PatientList:
        pass


    @abstractmethod
    async def select_by_id(self, id: str) -> PatientList:
        pass


    @abstractmethod
    async def insert(self, entity: PatientList):
        pass


    @abstractmethod
    async def update(self, entity: PatientList, updateInfo: PatientList):
        pass


    @abstractmethod
    async def delete(self, entity: PatientList):
        pass