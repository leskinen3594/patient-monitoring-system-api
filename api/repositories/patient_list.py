import uuid
from typing import TYPE_CHECKING

from ..handlers.errors import (
    NotFoundException, UnknowException
)

from domain.port import PatientListRepositoryAbstract
from ..models import all_tables as _models
from ..schemas.patient_list import (
    CreateUpdate, PatientList
)


if TYPE_CHECKING:
    from sqlalchemy.orm import Session


class PatientListRepository(PatientListRepositoryAbstract):
    def __init__(self, database: "Session"):
        self.db = database


    async def generate_ptl_id(self) -> str:
        return str(uuid.uuid4())


    async def insert(self, ptl: CreateUpdate) -> str:
        try:
            self.ptl = _models.PatientList(**ptl)
            self.db.add(self.ptl)
            self.db.commit()
        except:
            raise UnknowException(f"cannot create patient list.")
        return "patient list created"


    async def select_all(self) -> PatientList:
        try:
            self.ptls = self.db.query(_models.PatientList).all()
        except:
            raise NotFoundException(f"patient list empty.")
        return self.ptls


    async def select_by_id(self, id: str) -> PatientList:
        try:
            self.ptl = self.db.query(_models.PatientList).filter(_models.PatientList.doctor_id == id).first()

            if self.ptl is None:
                raise
        except:
            raise NotFoundException(f"ptl_id: '{id}' not found.")
        return self.ptl


    async def update(self, ptl: PatientList, ptl_update: CreateUpdate) -> str:
        try:
            ptl.doctor_id = ptl_update['doctor_id']
            ptl.pt_id = ptl_update['pt_id']

            self.db.commit()
        except:
            raise UnknowException(f"cannot update ptl_id: '{ptl.ptl_id}'.")
        return "patient list updated"


    async def delete(self, ptl: PatientList) -> str:
        try:
            self.db.delete(ptl)
            self.db.commit()
        except:
            raise UnknowException(f"cannot delete ptl_id: '{ptl.ptl_id}'.")
        return "patient list deleted"