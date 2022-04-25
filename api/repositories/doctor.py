import uuid
from typing import TYPE_CHECKING, Tuple

from ..handlers.errors import (
    DuplicateKeyException, NotFoundException, RequireKeyException
)

from domain.port import DoctorRepositoryAbstract
from ..models import all_tables as _models
from ..schemas.doctor import (
    CreateUpdate, Doctor
)


if TYPE_CHECKING:
    from sqlalchemy.orm import Session


class DoctorRepository(DoctorRepositoryAbstract):
    def __init__(self, database: "Session"):
        self.db = database


    async def generate_doctor_id(self) -> str:
        return str(uuid.uuid4())


    async def insert(self, doctor: CreateUpdate) -> Tuple[str]:
        try:
            self.doctor = _models.Doctor(**doctor)
            self.db.add(self.doctor)
            self.db.commit()
        except Exception as e:
            raise DuplicateKeyException(f"doctor_code: '{doctor['doctor_code']}' already exist. {e}")
        return (doctor['doctor_code'], "doctor created")


    async def select_all(self) -> Doctor:
        try:
            self.doctors = self.db.query(_models.Doctor).all()
        except Exception as e:
            raise NotFoundException(f"doctor empty. {e}")
        return self.doctors


    async def select_by_id(self, id: str) -> Doctor:
        try:
            self.doctor = self.db.query(_models.Doctor).filter(_models.Doctor.doctor_id == id).first()

            if self.doctor is None:
                raise
        except Exception as e:
            raise NotFoundException(f"doctor_id: '{id}' not found. {e}")
        return self.doctor


    async def update(self, doctor: Doctor, doctor_update: CreateUpdate) -> Tuple[str]:
        try:
            doctor.doctor_code = doctor_update['doctor_code']
            doctor.updated_at = doctor_update['updated_at']

            self.db.commit()
        except Exception as e:
            raise RequireKeyException(f"doctor_code require. {e}")
        return (doctor.doctor_id, "doctor updated")