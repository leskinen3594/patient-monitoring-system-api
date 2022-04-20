import uuid
from typing import TYPE_CHECKING

from ..handlers.errors import (
    NotFoundException, RequireKeyException, UnknowException
)

from domain.port import PrefixNameRepositoryAbstract
from ..models import all_tables as _models
from ..schemas.prefix_name import (
    CreateUpdate, PrefixName
)


if TYPE_CHECKING:
    from sqlalchemy.orm import Session


class PrefixRepository(PrefixNameRepositoryAbstract):
    def __init__(self, database: "Session"):
        self.db = database


    async def generate_prefix_id(self) -> str:
        return str(uuid.uuid4())


    async def insert(self, entity: CreateUpdate) -> str:
        try:
            self.prefix = _models.PrefixName(**entity)
            self.db.add(self.prefix)
            self.db.commit()
        except:
            raise RequireKeyException(f"prefix_nameth and prefix_ab_nameth require.")
        return "prefix name created"


    async def select_all(self) -> PrefixName:
        try:
            self.all_prefix_name = self.db.query(_models.PrefixName).all()
        except:
            raise NotFoundException(f"prefix name empty.")
        return self.all_prefix_name


    async def select_by_id(self, id: str):
        try:
            self.prefix_name = self.db.query(_models.PrefixName).filter(_models.PrefixName.prefix_id == id).first()

            if self.prefix_name is None:
                raise
        except:
            raise NotFoundException(f"prefix_id: '{id}' not found.")
        return self.prefix_name