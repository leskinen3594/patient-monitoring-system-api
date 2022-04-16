from typing import TypeVar, Generic
from abc import abstractmethod


IdType = TypeVar('IdType')
EntityType = TypeVar('EntityType')


class RepositoryAbstract(Generic[IdType, EntityType]):
    @abstractmethod
    async def insert(self, entity: EntityType):
        pass


    @abstractmethod
    async def select_by_id(self, identity: IdType) -> EntityType:
        pass


    @abstractmethod
    async def select_all(self) -> EntityType:
        pass


    @abstractmethod
    async def update(self, entity):
        pass


    @abstractmethod
    async def delete(self, identity: IdType):
        pass