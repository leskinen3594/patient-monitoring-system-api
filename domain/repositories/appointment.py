from abc import abstractmethod

from domain.base.repository import RepositoryAbstract
from domain.entities import Appointment


class AppointmentRepositoryAbstract(RepositoryAbstract[str, Appointment]):
    @abstractmethod
    async def generate_apmt_id(self):
        pass


    @abstractmethod
    async def select_all(self) -> Appointment:
        pass


    @abstractmethod
    async def select_by_id(self, id: str) -> Appointment:
        pass


    @abstractmethod
    async def insert(self, entity: Appointment):
        pass


    @abstractmethod
    async def update(self, entity: Appointment, updateInfo: Appointment):
        pass


    @abstractmethod
    async def delete(self, entity: Appointment):
        pass