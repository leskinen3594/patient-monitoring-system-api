import uuid
from typing import TYPE_CHECKING

from ..handlers.errors import (
    NotFoundException, UnknowException
)

from domain.port import AppointmentRepositoryAbstract
from ..models import all_tables as _models
from ..schemas.appointment import (
    CreateUpdate, Appointment
)


if TYPE_CHECKING:
    from sqlalchemy.orm import Session


class AppointmentRepository(AppointmentRepositoryAbstract):
    def __init__(self, database: "Session"):
        self.db = database


    async def generate_apmt_id(self) -> str:
        return str(uuid.uuid4())


    async def insert(self, apmt: CreateUpdate) -> str:
        try:
            self.apmt = _models.Appointment(**apmt)
            self.db.add(self.apmt)
            self.db.commit()
        except:
            raise UnknowException(f"cannot create an appointment.")
        return "appointment created"


    async def select_all(self) -> Appointment:
        try:
            self.all_apmt = self.db.query(_models.Appointment).all()
            
            if self.all_apmt is None:
                raise
        except:
            raise NotFoundException(f"appointment empty.")
        return self.all_apmt


    async def select_by_id(self, id: str) -> Appointment:
        try:
            self.apmt = self.db.query(_models.Appointment).filter(_models.Appointment.apmt_id == id).first()

            if self.apmt is None:
                raise
        except:
            raise NotFoundException(f"apmt_id: '{id}' not found.")
        return self.apmt


    async def update(self, apmt: Appointment, apmt_update: CreateUpdate) -> str:
        try:
            apmt.pt_id = apmt_update['pt_id']
            apmt.doctor_id = apmt_update['doctor_id']
            apmt.apmt_datettime = apmt_update['apmt_datettime']
            apmt.updated_at = apmt_update['updated_at']

            self.db.commit()
        except:
            raise UnknowException(f"cannot update apmt_id: '{apmt.apmt_id}'.")
        return "appointment updated"


    async def delete(self, apmt: Appointment) -> str:
        try:
            self.db.delete(apmt)
            self.db.commit()
        except:
            raise UnknowException(f"cannot delete apmt_id: '{apmt.apmt_id}'.")
        return "appointment deleted"