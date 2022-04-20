from abc import abstractmethod

from domain.base.repository import RepositoryAbstract
from domain.entities import EstimateLog


class LogRepositoryAbstract(RepositoryAbstract[str, EstimateLog]):
    @abstractmethod
    async def generate_log_id(self):
        pass


    @abstractmethod
    async def select_all(self) -> EstimateLog:
        pass


    @abstractmethod
    async def select_by_id(self, id: str) -> EstimateLog:
        pass


    @abstractmethod
    async def insert(self, entity: EstimateLog):
        pass


    @abstractmethod
    async def update(self, entity: EstimateLog, updateInfo: EstimateLog):
        pass


    @abstractmethod
    async def delete(self, entity: EstimateLog):
        pass