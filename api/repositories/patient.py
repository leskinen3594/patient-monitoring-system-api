import uuid
from typing import TYPE_CHECKING, Tuple

from ..handlers.errors import (
    DuplicateKeyException, NotFoundException, RequireKeyException
)

from domain.port import PatientRepositoryAbstract
from ..models import all_tables as _models
from ..schemas.patient import (
    CreateUpdate, Patient
)


if TYPE_CHECKING:
    from sqlalchemy.orm import Session


class PatientRepository(PatientRepositoryAbstract):
    def __init__(self, database: "Session"):
        self.db = database


    async def generate_patient_id(self) -> str:
        return str(uuid.uuid4())


    async def insert(self, patient: CreateUpdate) -> Tuple[str]:
        try:
            self.patient = _models.Patient(**patient)
            self.db.add(self.patient)
            self.db.commit()
        except Exception as e:
            raise DuplicateKeyException(f"'patient_code' or 'identity_number' already exist. {e}")
        return (patient['pt_code'], "patient created")


    async def select_all(self) -> Patient:
        try:
            self.patients = self.db.query(_models.Patient).all()
        except Exception as e:
            raise NotFoundException(f"patient empty. {e}")
        return self.patients


    async def select_by_id(self, id: str) -> Patient:
        try:
            self.patient = self.db.query(_models.Patient).filter(_models.Patient.pt_id == id).first()

            if self.patient is None:
                raise
        except Exception as e:
            raise NotFoundException(f"patient_id: '{id}' not found. {e}")
        return self.patient


    async def update(self, patient: Patient, patient_update: CreateUpdate) -> Tuple[str]:
        try:
            patient.pt_code = patient_update['pt_code']
            patient.identity_number = patient_update['identity_number']
            patient.pt_birth_date = patient_update['pt_birth_date']
            patient.pt_religion = patient_update['pt_religion']
            patient.pt_address = patient_update['pt_address']
            patient.pt_disease = patient_update['pt_disease']
            patient.pt_weight = patient_update['pt_weight']
            patient.pt_height = patient_update['pt_height']
            patient.pt_pressure = patient_update['pt_pressure']
            patient.pt_blood_type = patient_update['pt_blood_type']
            patient.pt_remark = patient_update['pt_remark']
            patient.updated_at = patient_update['updated_at']

            self.db.commit()
        except Exception as e:
            raise RequireKeyException(f"pt_code and identity_number require. {e}")
        return (patient.pt_id, "patient updated")