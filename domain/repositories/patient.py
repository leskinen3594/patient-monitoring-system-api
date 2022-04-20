from abc import abstractmethod

from domain.base.repository import RepositoryAbstract
from domain.entities import Patient


class PatientRepositoryAbstract(RepositoryAbstract[str, Patient]):
    @abstractmethod
    async def generate_patient_id(self):
        pass


    @abstractmethod
    async def select_all(self) -> Patient:
        pass


    @abstractmethod
    async def select_by_id(self, id: str) -> Patient:
        pass


    @abstractmethod
    async def insert(self, entity: Patient):
        pass


    @abstractmethod
    async def update(self, entity: Patient, updateInfo: Patient):
        pass