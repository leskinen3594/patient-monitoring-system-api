from abc import abstractmethod

from domain.base.repository import RepositoryAbstract
from domain.entities import User, Login


class UserRepositoryAbstract(RepositoryAbstract[str, User]):
    @abstractmethod
    async def generate_user_id(self):
        pass


    @abstractmethod
    async def select_all(self) -> User:
        pass


    @abstractmethod
    async def select_by_id(self, id: str) -> User:
        pass


    @abstractmethod
    async def insert(self, entity: User):
        pass


    @abstractmethod
    async def update(self, entity: User, updateInfo: User):
        pass


    @abstractmethod
    async def delete(self, entity: User):
        pass


    @abstractmethod
    async def login(self, loginRequest: Login):
        pass


    @abstractmethod
    async def doctor_detail(self, userId: str):
        pass


    @abstractmethod
    async def patient_detail(self, userId: str):
        pass