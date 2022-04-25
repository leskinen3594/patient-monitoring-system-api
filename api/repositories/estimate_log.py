import uuid
from typing import TYPE_CHECKING

from ..handlers.errors import (
    NotFoundException, UnknowException
)

from domain.port import LogRepositoryAbstract
from ..models import all_tables as _models
from ..schemas.estimate_log import (
    CreateUpdate, EstimateLog
)


if TYPE_CHECKING:
    from sqlalchemy.orm import Session


class LogRepository(LogRepositoryAbstract):
    def __init__(self, database: "Session"):
        self.db = database


    async def generate_log_id(self) -> str:
        return str(uuid.uuid4())


    async def insert(self, log: CreateUpdate) -> str:
        try:
            self.log = _models.Log(**log)
            self.db.add(self.log)
            self.db.commit()
        except Exception as e:
            raise UnknowException(f"cannot create estimate log. {e}")
        return "estimate log created"


    async def select_all(self) -> EstimateLog:
        try:
            self.logs = self.db.query(_models.Log).all()
        except Exception as e:
            raise NotFoundException(f"log empty. {e}")
        return self.logs


    async def select_by_id(self, id: str) -> EstimateLog:
        try:
            self.log = self.db.query(_models.Log).filter(_models.Log.log_id == id).first()

            if self.log is None:
                raise
        except Exception as e:
            raise NotFoundException(f"log_id: '{id}' not found. {e}")
        return self.log


    async def update(self, log: EstimateLog, log_update: CreateUpdate) -> str:
        try:
            log.doctor_id = log_update['doctor_id']
            log.pt_id = log_update['pt_id']
            log.log_level = log_update['log_level']
            log.log_desc = log_update['log_desc']
            log.updated_at = log_update['updated_at']

            self.db.commit()
        except Exception as e:
            raise UnknowException(f"cannot update log_id: '{log.log_id}'. {e}")
        return "estimate log updated"


    async def delete(self, log: EstimateLog) -> str:
        try:
            self.db.delete(log)
            self.db.commit()
        except Exception as e:
            raise UnknowException(f"cannot delete log_id: '{log.log_id}'. {e}")
        return "estimate log deleted"