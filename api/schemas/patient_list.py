from pydantic import BaseModel


class CreateUpdate(BaseModel):
    doctor_id: str
    pt_id: str


class CreateUpdateSuccess(BaseModel):
    ptl_id: str
    message: str

    class Config:
        orm_mode = True


class PatientList(BaseModel):
    ptl_id: str | None
    doctor_id: str | None
    pt_id: str | None

    class Config:
        orm_mode = True


class DeleteSuccess(BaseModel):
    message: str

    class Config:
        orm_mode = True